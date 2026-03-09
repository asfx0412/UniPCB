# -*- coding: utf-8 -*-
"""
UniPCB Reward Function for RLHF Training
Computes rewards based on format correctness and task accuracy.

Score components:
  1) format_score: strict <think>...</think><answer>...</answer> format (1 or 0)
  2) accuracy_score: task correctness (MCQ/BBOX/OPEN) in [0,1]
- Final reward: WT * accuracy_score + WF * format_score
"""

import os
import re
import json
import html
from typing import Any, Dict, List, Optional, Tuple, Union

# -------------------------
# Environment Configuration
# -------------------------
IOU_THR = float(os.environ.get("IOU_THR", "0.30"))
WT = float(os.environ.get("WT", "0.9"))  # Weight for accuracy
WF = float(os.environ.get("WF", "0.1"))  # Weight for format

# Optional prior knowledge for label canonicalization
PRIOR_JSON = os.environ.get("PRIOR_JSON", "")

# -------------------------
# Regex Patterns
# -------------------------
STRICT_RE = re.compile(
    r"^\s*<think>(.*?)</think>\s*<answer>(.*?)</answer>\s*$",
    re.S | re.I
)
ANSWER_RE = re.compile(r"<answer>(.*?)</answer>", re.S | re.I)


# -------------------------
# Prior Knowledge (optional label canonicalization)
# -------------------------
class Prior:
    """Lightweight label canonicalization."""
    def __init__(self, prior_obj: Optional[Dict[str, Any]] = None):
        self.map: Dict[str, str] = {}
        if prior_obj:
            self._build(prior_obj)

    @staticmethod
    def _norm(s: Any) -> str:
        t = html.unescape(str(s or "")).strip().lower()
        t = re.sub(r"[\s_\-、，,.:;!！：；·'\"""''’]+", "", t)
        return t

    def _build(self, obj: Dict[str, Any]):
        for k in ("defect_map", "component_map"):
            group = obj.get(k, {}) or {}
            for zh, info in group.items():
                if not isinstance(info, dict):
                    continue
                en = (info.get("en") or "").strip()
                aliases = [zh] + (info.get("aliases", []) or [])
                if en:
                    aliases.append(en)
                base = en if en else zh
                base_k = self._norm(base)
                for a in aliases:
                    self.map[self._norm(a)] = base_k

    def canon(self, s: Any) -> str:
        key = self._norm(s)
        return self.map.get(key, key)


def _load_prior() -> Prior:
    """Load prior knowledge from JSON file."""
    if PRIOR_JSON and os.path.exists(PRIOR_JSON):
        try:
            with open(PRIOR_JSON, "r", encoding="utf-8") as f:
                return Prior(json.load(f))
        except Exception:
            pass
    return Prior(None)


# -------------------------
# Parse Model Output
# -------------------------
def parse_output(resp: str) -> Dict[str, Any]:
    """
    Parse model response.
    Required format: <think>...</think><answer>...</answer>
    """
    resp = resp or ""
    m = STRICT_RE.match(resp)
    strict_ok = bool(m)
    think = (m.group(1).strip() if m else "")
    answer = (m.group(2).strip() if m else "")

    fallback_answer = ""
    m2 = ANSWER_RE.search(resp)
    if m2:
        fallback_answer = (m2.group(1) or "").strip()

    return {
        "strict_ok": strict_ok,
        "format_score": 1.0 if strict_ok else 0.0,
        "think": think if strict_ok else "",
        "answer": answer if strict_ok else fallback_answer,
        "raw_response": resp,
        "has_answer_tag": bool(m2),
    }


# -------------------------
# MCQ Scoring
# -------------------------
def mcq_letter(s: str) -> Optional[str]:
    """Extract MCQ letter (A-H) from string."""
    if not isinstance(s, str):
        return None
    t = s.upper().strip()

    # Most robust: first standalone A-H
    m = re.search(r"\b([A-H])\b", t)
    if m:
        return m.group(1)

    # Allow "A." "B)" etc.
    m = re.search(r"([A-H])(?=[\.\)\]、：:\-_ \t\r\n]|$)", t)
    if m:
        return m.group(1)

    # Allow "答案: C"
    m = re.search(r"(选|答案|正确答案)\s*[:：]?\s*([A-H])", t)
    if m:
        return m.group(2)

    return None


def score_mcq(pred_ans: str, gt: Union[str, List[str]]) -> Tuple[float, Dict[str, Any]]:
    """Score MCQ answer."""
    pred = mcq_letter(pred_ans or "")
    gt_list = gt if isinstance(gt, list) else [gt]
    gt_list = [(str(x or "").strip().upper()) for x in gt_list]

    if not pred:
        return 0.0, {"pred": None, "gt": gt_list, "note": "no_letter"}

    ok = any(pred == g for g in gt_list if g)
    return (1.0, {"pred": pred, "gt": gt_list, "note": "correct"}) if ok else (0.0, {"pred": pred, "gt": gt_list, "note": "wrong"})


# -------------------------
# BBOX Scoring
# -------------------------
def to_xyxy(box: Any) -> Optional[List[float]]:
    """Convert bbox to xyxy format."""
    if isinstance(box, dict):
        if "bbox" in box:
            return to_xyxy(box["bbox"])
        if all(k in box for k in ("x", "y", "w", "h")):
            x, y, w, h = map(float, [box["x"], box["y"], box["w"], box["h"]])
            return [x, y, x + w, y + h]
        if all(k in box for k in ("x1", "y1", "x2", "y2")):
            return [float(box[k]) for k in ("x1", "y1", "x2", "y2")]

    if isinstance(box, (list, tuple)) and len(box) == 4:
        x1, y1, x2, y2 = map(float, box)
        if x2 < x1 or y2 < y1:
            return [x1, y1, x1 + x2, y1 + y2]
        return [x1, y1, x2, y2]
    return None


def iou_xyxy(a: List[float], b: List[float]) -> float:
    """Compute IoU between two bounding boxes."""
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    x1, y1 = max(ax1, bx1), max(ay1, by1)
    x2, y2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0.0, x2 - x1) * max(0.0, y2 - y1)
    if inter <= 0:
        return 0.0
    area_a = max(0.0, ax2 - ax1) * max(0.0, ay2 - ay1)
    area_b = max(0.0, bx2 - bx1) * max(0.0, by2 - by1)
    union = area_a + area_b - inter
    return inter / max(union, 1e-6)


def score_bbox(pred_ans: str, gt: Any, prior: Prior) -> Tuple[float, Dict[str, Any]]:
    """Score bounding box prediction."""
    try:
        pred = json.loads(pred_ans)
    except:
        return 0.0, {"pred": pred_ans, "gt": gt, "note": "json_parse_error"}

    pred_box = to_xyxy(pred)
    gt_box = to_xyxy(gt)

    if not pred_box or not gt_box:
        return 0.0, {"pred": pred_box, "gt": gt_box, "note": "invalid_bbox"}

    iou = iou_xyxy(pred_box, gt_box)
    score = 1.0 if iou >= IOU_THR else 0.0

    return score, {
        "pred": pred_box,
        "gt": gt_box,
        "iou": iou,
        "thr": IOU_THR,
        "note": "pass" if score > 0 else "iou_too_low"
    }


# -------------------------
# Open-ended Scoring
# -------------------------
def score_open(pred_ans: str, gt: Union[str, List[str]], prior: Prior) -> Tuple[float, Dict[str, Any]]:
    """Score open-ended answer."""
    if not isinstance(pred_ans, str):
        return 0.0, {"pred": pred_ans, "gt": gt, "note": "non_string_pred"}

    pred_norm = prior.canon(pred_ans)
    gt_list = gt if isinstance(gt, list) else [gt]
    gt_norm_list = [prior.canon(g) for g in gt_list if isinstance(g, str)]

    ok = any(pred_norm == g for g in gt_norm_list if g)
    return (1.0, {"pred": pred_ans, "pred_norm": pred_norm, "gt": gt_list, "note": "match"}) if ok else (0.0, {"pred": pred_ans, "pred_norm": pred_norm, "gt": gt_list, "note": "no_match"})


# -------------------------
# Main Reward Function
# -------------------------
def compute_score(samples: List[Dict[str, Any]], **kwargs) -> List[float]:
    """
    Compute rewards for a batch of samples.
    
    Args:
        samples: List of samples with 'response' and 'extra_info'
    
    Returns:
        List of reward scores
    """
    prior = _load_prior()
    rewards = []

    for sample in samples:
        response = sample.get("response", "")
        extra = sample.get("extra_info", {}) or {}
        task_type = extra.get("task_type", "open")  # mcq, bbox, open
        gt = extra.get("gt", extra.get("answer", ""))

        # Parse output
        parsed = parse_output(response)
        format_score = parsed["format_score"]
        answer = parsed["answer"]

        # Compute accuracy score
        if task_type == "mcq":
            acc_score, _ = score_mcq(answer, gt)
        elif task_type == "bbox":
            acc_score, _ = score_bbox(answer, gt, prior)
        else:
            acc_score, _ = score_open(answer, gt, prior)

        # Combine scores
        reward = WT * acc_score + WF * format_score
        rewards.append(reward)

    return rewards


if __name__ == "__main__":
    # Test the reward function
    test_samples = [
        {
            "response": "<think>Analysis here</think><answer>A</answer>",
            "extra_info": {
                "task_type": "mcq",
                "gt": "A"
            }
        }
    ]
    scores = compute_score(test_samples)
    print(f"Reward score: {scores[0]}")
