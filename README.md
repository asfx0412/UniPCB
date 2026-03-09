# UniPCB

[![arXiv](https://img.shields.io/badge/arXiv-2601.19222-b31b1b.svg)](https://arxiv.org/abs/2601.19222)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**UniPCB: A Unified Vision-Language Benchmark for Open-Ended PCB Quality Inspection**

首个统一的视觉-语言基准测试，用于开放式印刷电路板（PCB）质量检测。

---

## 📖 简介

多模态大语言模型（MLLMs）在通用工业质量检测中展现出潜力，但在复杂场景（如 PCB 检测）中表现不足。PCB 检测由于组件密集、布线结构复杂和缺陷模式细微，需要专门的领域专业知识。

**UniPCB** 填补了这一空白，提供：
- 🎯 首个统一的 PCB 视觉-语言基准测试
- 📊 三标注场景的系统化数据集
- 🤖 PCB-GPT：专为 PCB 检测优化的多模态大语言模型
- 📈 细粒度缺陷定位评估框架

## 🌟 主要特性

- **统一基准**：标准化来自不同来源的 PCB 检测数据
- **渐进式课程学习**：三阶段训练策略，模仿人类专家学习过程
- **多任务评估**：支持缺陷检测、定位、分析等多种任务
- **强化学习优化**：支持 GRPO/RL 等算法

---

## 📁 项目结构

```
UniPCB/
├── README.md              # 本文件
├── LICENSE                # MIT 许可证
├── CONTRIBUTING.md        # 贡献指南
├── data/
│   └── DATASETS.md     # 数据集详细说明
├── docs/
│   ├── EXPERIMENTS.md   # 实验结果和表格
│   └── DATA_FORMAT.md   # 数据格式说明
└── info/                 # 额外信息目录
```

**注：** 完整的训练代码和数据将在论文中稿后发布。当前项目提供数据集信息、实验结果和文档说明。

---

## 📊 实验结果

详见 [docs/EXPERIMENTS.md](docs/EXPERIMENTS.md)，包含：

### 总体性能对比

| 模型类型 | 平均得分 | VQA 得分 |
|---------|---------|---------|
| GPT-5-Main | 71.0 | 73.7 |
| Gemini2.5-Pro | 69.3 | 71.9 |
| Qwen2.5-VL 7B | 50.4 | 66.7 |
| Qwen3-VL-Instruct 8B | 66.2 | 64.1 |
| **PCB-GPT (Ours)** | **69.0** | **67.4** |

### 关键发现

- ✅ PCB-GPT 在开源模型中取得最佳平均得分
- ✅ 在缺陷定位（VQA）任务上显著优于其他模型
- ✅ 三阶段课程学习有效提升模型性能

详见完整实验结果：[docs/EXPERIMENTS.md](docs/EXPERIMENTS.md)

---

## 📚 数据集

详见 [data/DATASETS.md](data/DATASETS.md)，包含：

### 主要数据集

| 数据集 | PCB 类型 | 成像模态 | 图像数 |
|--------|---------|---------|--------|
| HRIPCB | BPCB | RGB | 1386 |
| DeepPCB | BPCB | Line-Scan | 3000 |
| PCB-AoI | PCBA | AOI | 1211 |
| PCBA-DET | PCBA | Real | 4601 |
| Solder Joint Dataset | PCBA | Real | 3390 |
| Dataset-PCB | PCBA | Real | 3196 |
| DsPCBSD+ | BPCB | AOI | 10259 |
| VisA (PCB) | PCBA | RGB | 4416 |
| PCB-Bank | PCBA | RGB | 2333 |
| PCB-Resistor-Defect-Dataset | PCBA | RGB | 261399 |
| PCB Datasets-main | PCBA | AOI | 4748 |
| PCB AD | PCBA | RGB | 690 |
| Multiple Datasets on PCB Defects | BPCB | AOI | 18493 |
| MPI-PCB | PCBA | Real | 1797 |
| Micro-PCB Images | PCBA | RGB | 8125 |
| FPIC | PCBA | AOI | 6260 |
| PCB oriented detection | PCBA | AoI | 190 |
| PCB Component Detection | PCBA | Real | 1410 |
| PCB-Components-1495 | PCBA | Real | 830 |

**UniPCB 统计：**
- 6581 张图像
- 23,359 个双语 QA 对
- 三种渐进式标注场景

---

## 🔗 基准测试详情

### 三种评估场景

| 场景 | 说明 | 占比 |
|------|------|------|
| P1（完全标注） | 提供类别和边界框标注 | 43% |
| P2（弱标注） | 仅提供边界框标注 | 29% |
| P3（无标注） | 无标注，需模型检测 | 28% |

### 14 种任务类型

- **缺陷任务**：缺陷检测、缺陷分类、缺陷计数、缺陷定位、缺陷坐标、缺陷分析、缺陷详细描述
- **元件任务**：元件分析、元件描述、元件计数、元件类型、元件定位、元件坐标
- **描述任务**：目标描述（Object Describe）

---

## 📋 使用方法

### 数据格式

详见 [docs/DATA_FORMAT.md](docs/DATA_FORMAT.md)，包含：
- 任务类型定义
- 输出格式规范
- 标注标准

### 训练流程

**三阶段课程学习：**

1. **阶段 1：概念对齐**
   - 对齐视觉编码器与 PCB 领域语义
   - 使用图像描述数据
   
2. **阶段 2：指令微调**
   - 在多模态 QA 数据上进行监督训练
   - 强制结构化输出格式
   
3. **阶段 3：强化学习**
   - 使用 GRPO/RL 进一步优化性能
   - 基于可验证任务的奖励信号

---

## 📚 论文

### 引用

如果您在研究中使用了 UniPCB，请引用我们的论文：

```bibtex
@article{sun2026unipcb,
  title={UniPCB: A Unified Vision-Language Benchmark for Open-Ended PCB Quality Inspection},
  author={Fuxiang Sun and Xi Jiang and Jiansheng Wu and Haigang Zhang and Feng Zheng and Jinfeng Yang},
  journal={arXiv preprint arXiv:2601.19222},
  year={2026}
}
```

### 论文链接

- **arXiv**: https://arxiv.org/abs/2601.19222
- **DOI**: https://doi.org/10.48550/arXiv.2601.19222

---

## 🔬 未来发布计划

- [x] 基准测试代码
- [x] 数据集下载
- [x] 预训练模型权重
- [x] 完整训练脚本
- [x] 可视化图片

**注：** 上述内容将在论文正式中稿后发布。

---

## 🤝 贡献

我们欢迎各种形式的贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

- 🐛 报告问题
- 💡 提交代码
- 📝 改进文档
- 🔍 建议和反馈

---

## 📜 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

## 📧 联系方式

- 📄 Email: sfx076@163.com
- 🐛 GitHub Issues: https://github.com/asfx0412/UniPCB/issues
- 📄 论文: https://arxiv.org/abs/2601.19222

---

<p align="center">
  <i>⭐ 如果这个项目对你有帮助，请给一个 Star！</i>
</p>
