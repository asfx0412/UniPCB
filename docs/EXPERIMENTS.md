# 📊 实验结果

## UniPCB 基准测试结果

### 总体性能对比

| 模型类型 | 模型 | 参数量 | CoT Acc | F1 | OQA Score | Average | P1 | P2 | P3 | P1 | P2 | P3 | VQA |
|---------|-------|-------|----------|----|----------|--------|----|----|----|----|----|----|-----|
| Commercial MLLM | GPT-5-Main | - | 73.1 | 66.1 | 77.0 | 71.2 | 72.2 | 70.5 | 71.0 | 20.2 | 73.7 | 66.5 |
| Commercial MLLM | Gemini2.5-Pro | - | 76.4 | 68.5 | 71.9 | 69.6 | 66.5 | 67.7 | 69.3 | 64.9 | 23.6 | 70.8 | 64.9 |
| Commercial MLLM | EMIT 8B | 36.4 | 48.5 | 69.3 | 60.0 | 70.2 | 69.2 | 67.1 | 70.0 | 10.5 | 60.2 | 56.1 |
| IAD MLLM | IAD-R1 7B | 58.9 | 50.1 | 56.9 | 54.7 | 56.4 | 61.3 | 60.0 | 60.5 | 15.2 | 36.0 | 51.0 |
| IAD MLLM | AnomalyGPT 7B | 12.9 | 12.3 | 37.4 | 50.1 | 47.0 | 58.3 | 61.4 | 60.0 | - | 34.6 | 37.4 |
| IAD MLLM | DeepSeek2VL 16B | 17.5 | 24.4 | 57.8 | 47.3 | 53.3 | 64.6 | 62.2 | 63.0 | - | 39.6 | 43.0 |
| IAD MLLM | InternVL2.5 8B | 56.7 | 39.0 | 66.0 | 64.0 | 66.6 | 68.1 | 67.7 | 65.6 | 14.0 | 58.7 | 56.6 |
| IAD MLLM | InternVL3 8B | 52.9 | 47.2 | 64.7 | 56.0 | 66.1 | 67.2 | 62.1 | 67.5 | 18.0 | 56.5 | 55.9 |
| IAD MLLM | InternVL3.5 8B | 57.5 | 43.5 | 65.5 | 53.7 | 64.5 | 67.7 | 61.1 | 68.0 | 19.5 | 55.5 | 55.6 |
| IAD MLLM | LLaVA-OV 8B | 61.6 | 55.4 | 73.2 | 56.7 | 68.7 | 70.0 | 67.1 | 67.9 | - | 59.8 | 58.1 |
| IAD MLLM | MiMo-V2-Flash 15B | 40.0 | 47.7 | 42.0 | 64.0 | 45.4 | 57.8 | 67.0 | 61.4 | 16.1 | 42.6 | 48.4 |
| IAD MLLM | MiniCPM-V4.5 8B | 53.9 | 54.0 | 57.7 | 66.3 | 65.6 | 61.0 | 67.9 | 67.2 | 15.5 | 58.2 | 56.7 |
| Open Source MLLM | Qwen2.5-VL 7B | 53.2 | 44.2 | 66.7 | 50.4 | 63.7 | 68.1 | 60.7 | 66.5 | (1/8) | 54.3 | 55.0 |
| Open Source MLLM | Qwen3-VL-Instruct 8B | 61.5 | 48.7 | 64.8 | 66.2 | 64.6 | 65.0 | 68.2 | 64.1 | (1/8) | 61.0 | 58.6 |
| Open Source MLLM | Qwen3-VL-Think 8B | 65.6 | 54.6 | 64.9 | 65.5 | 58.0 | 65.6 | 66.5 | 65.0 | (1/8) | 58.7 | 58.5 |
| **PCB-GPT (Ours)** | 7B | **72.5** | **66.4** | **73.4** | **69.0** | **67.1** | **70.1** | **70.0** | **67.4** | **51.1** | **65.8** | **67.3** |

**关键发现：**
- PCB-GPT 在开放源模型中取得最佳平均得分
- 在缺陷定位（VQA）任务上显著优于其他模型
- 商业模型在语义一致性方面表现较强
- 主流 MLLM 在精细定位方面仍有较大改进空间

---

## 跨数据集泛化

| 模型 | Setting | Accuracy | Precision | Recall | F1 |
|-------|---------|----------|----------|------|
| GPT-5-Main | 0-shot | 65.1 | 39.9 | 28.2 | 33.0 |
| AnomalyGPT | 0-shot | 70.7 | 46.0 | 44.6 | 45.3 |
| **PCB-GPT (Ours)** | 0-shot | **63.8** | 40.6 | **72.1** | 52.1 |
| GPT-5-Main | 1-shot | 48.3 | 35.6 | 85.7 | 50.3 |
| AnomalyGPT | 1-shot | 42.3 | 30.6 | 88.2 | 45.5 |
| **PCB-GPT (Ours)** | 1-shot | 77.8 | 50.6 | 76.0 | 61.0 |

**关键发现：**
- PCB-GPT 在零样本设置下实现更高的召回率，对真实缺陷更敏感
- 一样本设置下，PCB-GPT 在准确率和召回率上均有提升

---

## 消融实验

| 基础模型 | 模型 | CoT | Acc | F1 | OQA Score | Average |
|---------|-------|-----|----|----|----------|--------|
| Qwen2.5-VL 7B | BaseData | ✗ | 48.7 | 22.3 | 59.9 | 43.6 |
| Qwen2.5-VL 7B | +Stage1 | ✗ | 60.1 | 30.0 | 66.1 | 52.1 |
| Qwen2.5-VL 7B | +Stage2 | ✗ | 57.1 | 22.7 | 69.3 | 49.7 |
| Qwen2.5-VL 7B | +Stage1,2 | ✗ | 57.1 | 15.2 | 62.8 | 45.1 |
| Qwen2.5-VL 7B | +Stage1,2,3 | ✗ | 65.6 | 27.3 | 69.8 | 54.2 |
| Qwen2.5-VL 7B | +Stage1,2 | ✓ | 63.3 | 38.9 | 67.0 | 56.4 |
| Qwen2.5-VL 7B | +Stage1,2,3 | ✓ | **69.5** | **51.1** | **69.0** | **63.2** |

**关键发现：**
- 仅添加原始数据也能带来稳定提升
- 概念对齐阶段主要改善语义指标
- 指令微调显著提升所有指标
- 强化学习进一步提升性能，特别是输出一致性
- CoT 监督提升模型的结构化输出能力

---

## 主要数据集

### 收集的 PCB 数据集

| 数据集 | PCB 类型 | 模态 | 目标 | #类别 | #图像 | 链接 |
|--------|---------|------|------|-------|--------|-------|
| HRIPCB | BPCB | RGB | Defect | 6 | 1386 | https://pkusz.edu.cn/ |
| HRIPCB-Augmented | BPCB | RGB | Defect | 6 | 10668 | https://github.com/ |
| DeepPCB | BPCB | Line-Scan | Defect | 6 | 3000 | https://github.com/ |
| PCB-AoI | PCBA | AOI | Defect | 1 | 1211 | https://kaggle.com/ |
| PCBA-DET | PCBA | Real | Defect | 8 | 4601 | https://github.com/ |
| Solder Joint Dataset | PCBA | Real | Defect | 5 | 3390 | https://github.com/ |
| Dataset-PCB | PCBA | Real | Defect | 2 | 3196 | https://github.com/ |
| DsPCBSD+ | BPCB | AOI | Defect | 9 | 10259 | https://github.com/ |
| PCB-Defect-Detection-Image-Registration | BPCB | Line-Scan | Defect | 6 | 20 | https://github.com/ |
| Defects Dataset | PCBA | Real | Defect | 5 | 484 | https://roboflow.com/ |
| Mono PCB Dataset | PCBA | RGB | Component | 16 | 248 | https://roboflow.com/ |
| Mixed PCB defect | BPCB | RGB | Defect | 6 | 1741 | https://mendeley.com/ |
| Bangla PCB yolo | BPCB | RGB | Defect | 6 | 1196 | https://kaggle.com/ |
| MRC-DETR | BPCB | AOI | Defect | 3 | 800 | https://github.com/ |
| U-PCBD | BPCB | Ultrasonic | Defect | 5 | 4320 | https://iiplab.net/ |
| FICS | PCBA | RGB | Mix | 31 | 9912 | https://trust-hub.org/ |
| VisA (PCB) | PCBA | RGB | Mix | 10 | 4416 | https://github.com/ |
| PCB-Bank | PCBA | RGB | Mix | 11 | 2333 | https://github.com/ |
| PCB-Resistor-Defect-Dataset | PCBA | RGB | Mix | 11 | 261399 | https://github.com/ |
| PCB Datasets-main | PCBA | AOI | Mix | 8 | 4748 | https://github.com/ |
| PCB AD | PCBA | RGB | Mix | 5 | 690 | https://kaggle.com/ |
| Multiple Datasets on PCB Defects | BPCB | AOI | Mix | 2 | 18493 | https://kaggle.com/ |
| MPI-PCB | PCBA | Real | Mix | 2 | 1797 | https://github.com/ |
| Micro-PCB Images | PCBA | RGB | Component | 13 | 8125 | https://kaggle.com/ |
| FPIC | PCBA | AOI | Component | 25 | 6260 | https://ece.ufl.edu/ |
| PCB oriented detection | PCBA | AoI | Component | 41 | 190 | https://kaggle.com/ |
| PCB Component Detection | PCBA | Real | Component | 9 | 1410 | https://ninja.com/ |
| PCB-Components-1495 | PCBA | Real | Component | 28 | 830 | https://kaggle.com/ |
| PCB-Component-Detection-CVM | BPCB | RGB | Component | 9 | 101 | https://roboflow.com/ |
| DSLR | PCBA | RGB | Component | 4 | 748 | https://tuwien.ac.at/ |
| PCB-Vision | PCBA | RGB | Component | 4 | 106 | https://github.com/ |
| Lite-On Dataset | PCBA | AOI | Mix | 8 | 12200 | Private |

**注：** 私有数据集（Private）无法公开发布，UniPCB 仅使用公开数据子集。

---

## 论文附录图片

论文附录包含以下可视化内容：

1. **缺陷和组件分类可视化** - 展示 13 个缺陷类别和 6 个组件类别的层次结构
2. **数据集分布可视化** - 图像分辨率、成像模态、任务分布等统计图
3. **任务类型分布** - 14 种任务类型的比例分布
4. **QA 示例可视化** - 各类任务的问答示例
5. **训练阶段可视化** - 三阶段课程学习的逐步提升效果
6. **缺陷定位可视化** - 不同模型在同一缺陷上的定位结果对比
7. **多缺陷分类可视化** - 复合场景下多缺陷的识别能力
8. **组件定位可视化** - 密集组件场景下的定位效果

**可用的可视化图片将在论文中稿后发布。**
