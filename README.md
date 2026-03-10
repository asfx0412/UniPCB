# UniPCB: A Unified Vision-Language Benchmark for PCB Quality Inspection

[![Industry_Inspection](https://img.shields.io/badge/Task-PCB_Quality_Inspection-white)](https://github.com/M-3LAB/awesome-industrial-anomaly-detection)
[![UniPCB](https://img.shields.io/badge/Dataset-UniPCB-blue)]()
[![IJCAI 2026](https://img.shields.io/badge/Paper-IJCAI%202026-red)]()
[![PCB-GPT](https://img.shields.io/badge/Model-PCB--GPT-green)]()

![UniPCB Teaser](assets/teaser.pdf)

## 💡 Highlights
- First unified vision-language benchmark covering both BPCB and PCBA inspection levels
- 3 progressive annotation scenarios (fully / weakly / unlabeled) to evaluate model robustness under varying information density
- 14 inspection subtasks spanning detection, counting, classification, localization, defect analysis and reinspection recommendations
- PCB-GPT: specialized MLLM with 3-stage curriculum learning, doubling defect localization performance over general-purpose models

## 📜 News
- **[2026-03-10]** Repository and preprint paper released
- **[2026-01-15]** UniPCB paper accepted by IJCAI 2026
- **[2025-12-20]** PCB-GPT achieves new SOTA on all PCB inspection benchmarks

## Overview
UniPCB is the first unified vision-language benchmark tailored for open-ended PCB quality inspection tasks. It systematically integrates and standardizes multi-source PCB data across BPCB and PCBA inspection levels, covering 3 annotation scenarios and 14 quality inspection subtasks.

We also propose **PCB-GPT**, a specialized vision-language assistant for PCB inspection trained with a three-stage curriculum learning strategy, which achieves state-of-the-art performance on fine-grained defect localization and interpretable reasoning tasks.

## Data Construction Pipeline
![Data Generation Pipeline](assets/data_pipeline.pdf)

Our systematic data construction pipeline unifies:
1. Multi-source data collection across different imaging modalities
2. Standardized annotation protocols for defects and components
3. Unified taxonomy with 7 defect categories and 6 component functional domains
4. Dual-track quality control for both training set and benchmark generation

## Dataset Statistics
![Category Distribution](assets/category_distribution.pdf)

The UniPCB benchmark contains:
- 6k high-quality PCB images
- 23k multi-modal question-answer pairs
- 3 annotation scenarios (fully labeled / weakly labeled / unlabeled)
- 14 inspection subtasks covering detection, counting, classification, localization, defect analysis and reinspection recommendations

## 🚀 Quick Start
### Environment Setup
```bash
# Clone repository
git clone https://github.com/your-username/UniPCB.git
cd UniPCB

# Install dependencies
pip install -r requirements.txt
```

### Dataset Preparation
1. Download the UniPCB dataset from [Hugging Face]() (coming soon after paper publication)
2. Unzip the dataset to `dataset/` directory:
```bash
unzip unipcb_dataset.zip -d dataset/
```

### Run Evaluation
Evaluate your model on the UniPCB benchmark:
```bash
# Evaluate all scenarios
python evaluation/evaluate.py --model <your-model-path> --scenario all

# Evaluate specific scenario
python evaluation/evaluate.py --model <your-model-path> --scenario fully_labeled
```

### Reproduce PCB-GPT Results
We provide the pre-trained PCB-GPT model for reproduction:
```bash
# Download pre-trained model
wget <model-url> -O models/pcb_gpt.pth

# Run evaluation
python evaluation/evaluate.py --model models/pcb_gpt.pth --scenario all
```

## Performance
| Model | Overall Accuracy | Defect Localization F1 | Reasoning Score |
|-------|------------------|-------------------------|-----------------|
| Qwen-VL-72B | 42.3% | 28.7% | 39.2% |
| InternVL-3.5-78B | 45.1% | 31.2% | 41.5% |
| LLaVA-Next-70B | 40.9% | 26.4% | 37.8% |
| **PCB-GPT (Ours)** | **68.7%** | **67.3%** | **70.2%** |

## Citation
```
@inproceedings{unipcb2026,
  title={UniPCB: A Unified Vision-Language Benchmark for PCB Quality Inspection},
  author={},
  booktitle={IJCAI},
  year={2026}
}
```
