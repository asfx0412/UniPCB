# UniPCB

[![arXiv](https://img.shields.io/badge/arXiv-2601.19222-b31b1b.svg)](https://arxiv.org/abs/2601.19222)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**UniPCB: A Unified Vision-Language Benchmark for Open-Ended PCB Quality Inspection**

The first unified vision-language benchmark for open-ended PCB quality inspection.

---

## Overview

[UniPCB](https://arxiv.org/abs/2601.19222) introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on printed circuit board (PCB) quality inspection tasks.

### Key Features

- 🎯 **Unified Benchmark**: Standardized evaluation across three annotation scenarios
- 📊 **23K QA Pairs**: High-quality bilingual dataset
- 🤖 **PCB-GPT**: Specialized MLLM with three-stage curriculum learning
- 📈 **Multi-Task**: 14 inspection subtasks (detection, localization, analysis, etc.)

---

## Quick Links

- 📄 [Paper](https://arxiv.org/abs/2601.19222)
- 🔬 [Data Statistics](#data-sources)
- 📊 [Experimental Results](#experimental-results)
- 📋 [Project Structure](#project-structure)

---

## Data Sources

### Public Datasets Used in UniPCB

| Dataset | PCB Type | Modality | Target | #Categories | #Images | Link |
|---------|---------|----------|---------|-----------|---------|------|
| [HRIPCB](https://pkusz.edu.cn/) | BPCB | RGB | Defect | 6 | 1386 |
| [HRIPCB-Augmented](https://github.com/) | BPCB | RGB | Defect | 6 | 10668 |
| [DeepPCB](https://github.com/DeepPCB) | BPCB | Line-Scan | Defect | 6 | 3000 |
| [PCB-AoI](https://kaggle.com/PCB-AoI) | PCBA | AOI | Defect | 1 | 1211 |
| [PCBA-DET](https://github.com/PCBA-DET) | PCBA | Real | Defect | 8 | 4601 |
| [Solder Joint Dataset](https://github.com/Solder-Joint-Dataset) | PCBA | Real | Defect | 5 | 3390 |
| [Dataset-PCB](https://github.com/Dataset-PCB) | PCBA | Real | Defect | 2 | 3196 |
| [DsPCBSD+](https://github.com/DsPCBSD+) | BPCB | AOI | Defect | 9 | 10259 |
| [PCB-Defect-Detection-Image-Registration](https://github.com/PCB-Defect-Detection-Image-Registration) | BPCB | Line-Scan | Defect | 6 | 20 |
| [Defects Dataset](https://roboflow.com/datasets/Defects-Dataset) | PCBA | Real | Defect | 5 | 484 |
| [Mono PCB Dataset](https://roboflow.com/datasets/Mono-PCB-Dataset) | PCBA | RGB | Component | 16 | 248 |
| [Mixed PCB defect](https://mendeley.com/datasets/Mixed-PCB-defect) | BPCB | RGB | Defect | 6 | 1741 |
| [Bangla PCB yolo](https://kaggle.com/datasets/Bangla-PCB-yolo) | BPCB | RGB | Defect | 6 | 1196 |
| [MRC-DETR](https://github.com/MRC-DETR) | BPCB | AOI | Defect | 3 | 800 |
| [U-PCBD](http://iiplab.net/U-PCPCB) | PCBA | Ultrasonic | Defect | 5 | 4320 |
| [FICS](https://trust-hub.org/datasets/FICS) | PCBA | RGB | Mix | 31 | 9912 |
| [VisA (PCB)](https://github.com/VisA-PCB) | PCBA | RGB | Mix | 10 | 4416 |
| [PCB-Bank](https://github.com/PCB-Bank) | PCBA | RGB | Mix | 11 | 2333 |
| [PCB-Resistor-Defect-Dataset](https://github.com/PCB-Resistor-Defect-Dataset) | PCBA | RGB | Mix | 11 | 261399 |
| [PCB Datasets-main](https://github.com/PCB-Datasets-main) | PCBA | AOI | Mix | 8 | 4748 |
| [PCB AD](https://kaggle.com/PCB-AD) | PCBA | RGB | Mix | 5 | 690 |
| [Multiple Datasets on PCB Defects](https://kaggle.com/datasets/Multiple-Datasets-on-PCB-Defects) | PCBA | AOI | Mix | 2 | 18493 |
| [MPI-PCB](https://github.com/MPI-PCB) | PCBA | Real | Mix | 2 | 1797 |
| [Micro-PCB Images](https://kaggle.com/datasets/Micro-PCB-Images) | PCBA | RGB | Component | 13 | 8125 |
| [FPIC](https://ece.ufl.edu/~jessurun/FPIC) | PCBA | AOI | Component | 25 | 6260 |
| [PCB oriented detection](https://kaggle.com/datasets/PCB-oriented-detection) | PCBA | AoI | Component | 41 | 190 |
| [PCB Component Detection](https://ninja.com/datasets/PCB-Component-Detection) | PCBA | Real | Component | 9 | 1410 |
| [PCB-Components-1495](https://kaggle.com/datasets/PCB-Components-1495) | PCBA | Real | Component | 28 | 830 |
| [PCB-Component-Detection-CVM](https://roboflow.com/datasets/PCB-Component-Detection-CVM) | PCBA | RGB | Component | 9 | 101 |
| [DSLR](https://tuwien.ac.at/DSLR) | PCBA | RGB | Component | 4 | 748 |
| [PCB-Vision](https://github.com/PCB-Vision) | PCBA | RGB | Component | 4 | 106 |

**Total**: 22 public datasets, ~85K+ images

---

## Experimental Results

### Overall Performance on UniPCB Benchmark

| Model | Params | CoT Acc | F1 | OQA Score | Average | VQA |
|-------|-------|----------|----|----------|--------|-----|
| GPT-5-Main | - | 73.1 | 66.1 | 77.0 | 71.2 |
| Gemini-2.5-Pro | - | 76.4 | 68.5 | 71.9 | 69.3 |
| EMIT-8B | 36.4 | 48.5 | 69.3 | 60.0 |
| IAD-R1-7B | 58.9 | 50.1 | 56.9 | 54.7 |
| AnomalyGPT-7B | 12.9 | 12.3 | 37.4 | 50.1 |
| DeepSeek2VL-16B | 17.5 | 24.4 | 57.8 | 47.3 |
| InternVL2.5-8B | 56.7 | 39.0 | 66.0 | 64.0 |
| InternVL3-8B | 52.9 | 47.2 | 64.7 | 56.0 |
| InternVL3.5-8B | 57.5 | 43.5 | 65.5 | 53.7 |
| LLaVA-OV-8B | 61.6 | 55.4 | 73.2 | 56.7 |
| MiMo-V2-Flash-15B | 40.0 | 47.7 | 42.0 | 64.0 |
| MiniCPM-V4.5-8B | 53.9 | 54.0 | 57.7 | 66.3 |
| Qwen2.5-VL-7B | 53.2 | 44.2 | 66.7 | 50.4 |
| Qwen3-VL-Instruct-8B | 61.5 | 48.7 | 64.8 | 66.2 |
| Qwen3-VL-Think-8B | 65.6 | 54.6 | 64.9 | 65.5 |
| **PCB-GPT (Ours)** | 7B | **72.5** | **66.4** | **73.4** | **69.0** |

### Key Findings

- ✅ **PCB-GPT achieves the best average score** among open-source models
- ✅ **Significant improvement in defect localization** (VQA task)
- ✅ **Three-stage curriculum learning effectively boosts performance**
- 📊 CoT supervision enhances structured output capabilities

### Cross-Dataset Generalization (PCB-Bank)

| Model | Setting | Accuracy | Precision | Recall | F1 |
|-------|---------|----------|----------|----------|------|
| GPT-5-Main | 0-shot | 65.1 | 39.9 | 28.2 | 33.0 |
| AnomalyGPT | 0-shot | 70.7 | 46.0 | 44.6 | 45.3 |
| **PCB-GPT (Ours)** | 0-shot | **63.8** | 40.6 | **72.1** | **52.1** |
| GPT-5-Main | 1-shot | 48.3 | 35.6 | 85.7 | 50.3 |
| AnomalyGPT | 1-shot | 42.3 | 30.6 | 88.2 | 45.5 |
| **PCB-GPT (Ours)** | 1-shot | **77.8** | 50.6 | **76.0** | **61.0** |

### Ablation Study on Qwen2.5-VL-7B

| Base Model | CoT | Acc | F1 | OQA Score | Average |
|-------------|-----|----|----|----------|--------|
| BaseData | ✗ | 48.7 | 22.3 | 59.9 | 43.6 |
| +Stage1 | ✗ | 60.1 | 30.0 | 66.1 | 52.1 |
| +Stage2 | ✗ | 57.1 | 22.7 | 69.3 | 49.7 |
| +Stage1,2 | ✗ | 57.1 | 15.2 | 62.8 | 45.1 |
| +Stage1,2,3 | ✗ | 65.6 | 27.3 | 69.8 | 54.2 |
| +Stage1,2 | ✓ | **63.3** | **38.9** | **67.0** | **56.4** |
| +Stage1,2,3 | ✓ | **69.5** | **51.1** | **69.0** | **63.2** |

---

## Methodology

### Three-Stage Curriculum Learning

1. **Stage 1: Concept Alignment**
   - Align vision encoder with PCB domain semantics
   - Use caption-style concept data

2. **Stage 2: Instruction Tuning**
   - Supervised fine-tuning on multimodal QA data
   - Enforce structured output format

3. **Stage 3: Reinforcement Learning**
   - Apply GRPO/RL for further optimization
   - Use verifiable tasks with reward signals

### Evaluation Scenarios

- **P1 (Fully Labeled)**: Category + bounding box annotations (43%)
- **P2 (Weakly Labeled)**: Box-only annotations (29%)
- **P3 (Unlabeled)**: No annotations (28%)

---

## Citation

If you use UniPCB in your research, please cite our paper:

```bibtex
@article{sun2026unipcb,
  title={UniPCB: A Unified Vision-Language Benchmark for Open-Ended PCB Quality Inspection},
  author={Fuxiang Sun and Xi Jiang and Jiansheng Wu and Haigang Zhang and Feng Zheng and Jinfeng Yang},
  journal={arXiv preprint arXiv:2601.19222},
  year={2026}
}
```

---

## Project Structure

```
UniPCB/
├── README.md              # This file
├── LICENSE                # MIT License
└── assets/               # Figures and visualizations
```

---

## Future Release

The following will be released after paper acceptance:

- [ ] Benchmark evaluation code
- [ ] Dataset download scripts
- [ ] Pre-trained model weights
- [ ] Complete training scripts
- [ ] Visualization figures

---

## Contact

- **Email**: sfx076@163.com
- **GitHub Issues**: https://github.com/asfx0412/UniPCB/issues
- **Paper**: https://arxiv.org/abs/2601.19222

---

## License

This project is licensed under the [MIT License](LICENSE).
