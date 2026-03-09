# 数据格式说明

本文档描述 UniPCB 数据集的标准格式。

---

## 数据集结构

```
data/
├── stage1_cn.json           # 第一阶段中文数据
├── stage1_en.json           # 第一阶段英文数据
├── stage1_general.json      # 第一阶段通用数据
├── stage2_cn.json           # 第二阶段中文数据
├── stage2_en.json           # 第二阶段英文数据
├── stage2_general.json      # 第二阶段通用数据
├── stage3_train.parquet      # 第三阶段训练数据
├── stage3_test.parquet       # 第三阶段测试数据
└── train_prior_knowledge.json # 先验知识（用于标签规范化）
```

---

## 数据样本格式

### 第一、二阶段（JSON 格式）

每个样本包含以下字段：

```json
{
  "id": "sample_001",
  "image": "path/to/image.jpg",
  "conversations": [
    {
      "from": "human",
      "value": "分析这张 PCB 图片中有哪些元件？"
    },
    {
      "from": "gpt",
      "value": "这张 PCB 图片中包含电阻、电容和二极管等元件。"
    }
  ]
}
```

**字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 样本唯一标识符 |
| `image` | string | 图像文件路径（相对于数据根目录） |
| `conversations` | array | 对话列表，包含 human 和 gpt 的对话 |

**对话消息格式：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `from` | string | 消息发送者（"human" 或 "gpt"） |
| `value` | string | 消息内容 |

---

### 第三阶段（Parquet 格式）

第三阶段使用 Parquet 格式，支持强化学习训练：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 样本唯一标识符 |
| `images` | array | 图像列表（支持多图） |
| `prompt` | string | 提示文本 |
| `response` | string | 模型响应（训练时为空） |
| `extra_info` | object | 额外信息（任务类型、真实答案等） |

**extra_info 结构：**

```json
{
  "task_type": "mcq",  // mcq, bbox, or open
  "gt": "A",          // 真实答案
  "question": "这是什么类型的缺陷？",
  "options": ["A. 短路", "B. 开路", "C. 虚焊"]
}
```

---

## 测试数据格式

评估使用的测试数据格式：

```json
{
  "id": "test_001",
  "dataset_type": "P1",  // P1, P2, or P3
  "image": "path/to/image.jpg",
  "question": "找出所有焊接缺陷",
  "conversations": [
    {
      "from": "human",
      "value": "找出所有焊接缺陷"
    }
  ],
  "extra_info": {
    "task_type": "bbox",
    "gt": [
      {"x1": 100, "y1": 200, "x2": 300, "y2": 400, "label": "solder_defect"}
    ]
  }
}
```

---

## 任务类型

### MCQ（多选题）
- **task_type**: `"mcq"`
- **gt**: 选项字母（如 "A"）或字母列表
- **answer 格式**: `<answer>A</answer>`

### BBOX（边界框）
- **task_type**: `"bbox"`
- **gt**: 边界框列表 `[x1, y1, x2, y2]` 或格式为字典
- **answer 格式**: `<answer>[x1, y1, x2, y2]</answer>`（JSON）

### OPEN（开放回答）
- **task_type**: `"open"`
- **gt**: 正确答案字符串或列表
- **answer 格式**: `<answer>答案文本</answer>`

---

## 先验知识格式

`train_prior_knowledge.json` 用于标签规范化：

```json
{
  "defect_map": {
    "短路": {
      "en": "short_circuit",
      "aliases": ["short", "short_circ"]
    },
    "虚焊": {
      "en": "cold_solder",
      "aliases": ["dry_joint", "poor_soldering"]
    }
  },
  "component_map": {
    "电阻": {
      "en": "resistor",
      "aliases": ["R", "res"]
    },
    "电容": {
      "en": "capacitor",
      "aliases": ["C", "cap"]
    }
  }
}
```

---

## 数据增强建议

### 图像增强
- 随机旋转（±15°）
- 随机翻转（水平、垂直）
- 颜色抖动（亮度、对比度）
- 高斯噪声

### 文本增强
- 同义词替换
- 问题改写
- 翻译回译（中英互译）

---

## 数据质量检查

使用以下脚本检查数据质量：

```bash
python scripts/check_data.py --data data/stage1_cn.json
```

检查项：
- 图像文件是否存在
- 对话格式是否正确
- 标签是否符合规范
- 数据分布是否平衡

---

## 数据隐私和合规

确保数据集：
- 不包含个人隐私信息
- 不包含机密设计图纸
- 遵守相关法律法规
- 获得必要的使用授权

---

## 引用

如果使用数据集，请引用：

```bibtex
@article{sun2026unipcb,
  title={UniPCB: A Unified Vision-Language Benchmark for Open-Ended PCB Quality Inspection},
  author={Sun, Fuxiang and Jiang, Xi and Wu, Jiansheng and Zhang, Haigang and Zheng, Feng and Yang, Jinfeng},
  journal={arXiv preprint arXiv:2601.19222},
  year={2026}
}
```
