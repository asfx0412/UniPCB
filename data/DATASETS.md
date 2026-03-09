# 数据集目录说明

## 📊 收集的 PCB 数据集

下表列出了我们调研的所有 PCB 质量检测数据集，包括公开和私有数据集。**UniPCB 仅使用标注为公开的数据集**。

| 数据集 | PCB 类型 | 成像模态 | 目标 | 标签数 | 图像数 | 链接 | 可访问性 |
|--------|---------|---------|------|-------|--------|-------|---------|
| HRIPCB | BPCB | RGB | 缺陷 | 6 | 1386 | [论文](https://pkusz.edu.cn/) | 公开 |
| HRIPCB-Augmented | BPCB | RGB | 缺陷 | 6 | 10668 | [GitHub](https://github.com/) | 公开 |
| DeepPCB | BPCB | Line-Scan | 缺陷 | 6 | 3000 | [GitHub](https://github.com/) | 公开 |
| PCB-AoI | PCBA | AOI | 缺陷 | 1 | 1211 | [Kaggle](https://kaggle.com/) | 公开 |
| PCBA-DET | PCBA | Real | 缺陷 | 8 | 4601 | [GitHub](https://github.com/) | 公开 |
| Solder Joint Dataset | PCBA | Real | 缺陷 | 5 | 3390 | [GitHub](https://github.com/) | 公开 |
| Dataset-PCB | PCBA | Real | 缺陷 | 2 | 3196 | [GitHub](https://github.com/) | 公开 |
| DsPCBSD+ | BPCB | AOI | 缺陷 | 9 | 10259 | [GitHub](https://github.com/) | 公开 |
| PCB-Defect-Detection-Image-Registration | BPCB | Line-Scan | 缺陷 | 6 | 20 | [GitHub](https://github.com/) | 公开 |
| Defects Dataset | PCBA | Real | 缺陷 | 5 | 484 | [Roboflow](https://roboflow.com/) | 公开 |
| Mono PCB Dataset | PCBA | RGB | 元件 | 16 | 248 | [Roboflow](https://roboflow.com/) | 公开 |
| Mixed PCB defect | BPCB | RGB | 缺陷 | 6 | 1741 | [Mendeley](https://mendeley.com/) | 公开 |
| Bangla PCB yolo | BPCB | RGB | 缺陷 | 6 | 1196 | [Kaggle](https://kaggle.com/) | 公开 |
| MRC-DETR | BPCB | AOI | 缺陷 | 3 | 800 | [GitHub](https://github.com/) | 公开 |
| U-PCBD | BPCB | Ultrasonic | 缺陷 | 5 | 4320 | [iiplab.net](https://iiplab.net/) | 公开 |
| FICS | PCBA | RGB | 混合 | 31 | 9912 | [TrustHub](https://trust-hub.org/) | 公开 |
| VisA (PCB) | PCBA | RGB | 混合 | 10 | 4416 | [GitHub](https://github.com/) | 公开 |
| PCB-Bank | PCBA | RGB | 混合 | 11 | 2333 | [GitHub](https://github.com/) | 公开 |
| PCB-Resistor-Defect-Dataset | PCBA | RGB | 混合 | 11 | 261399 | [GitHub](https://github.com/) | 公开 |
| PCB Datasets-main | PCBA | AOI | 混合 | 8 | 4748 | [GitHub](https://github.com/) | 公开 |
| PCB AD | PCBA | RGB | 混合 | 5 | 690 | [Kaggle](https://kaggle.com/) | 公开 |
| Multiple Datasets on PCB Defects | BPCB | AOI | 混合 | 2 | 18493 | [Kaggle](https://kaggle.com/) | 公开 |
| MPI-PCB | PCBA | Real | 混合 | 2 | 1797 | [GitHub](https://github.com/) | 公开 |
| Micro-PCB Images | PCBA | RGB | 元件 | 13 | 8125 | [Kaggle](https://kaggle.com/) | 公开 |
| FPIC | PCBA | AOI | 元件 | 25 | 6260 | [ECE UFL](https://ece.ufl.edu/) | 公开 |
| PCB oriented detection | PCBA | AoI | 元件 | 41 | 190 | [Kaggle](https://kaggle.com/) | 公开 |
| PCB Component Detection | PCBA | Real | 元件 | 9 | 1410 | [Ninja](https://ninja.com/) | 公开 |
| PCB-Components-1495 | PCBA | Real | 元件 | 28 | 830 | [Kaggle](https://kaggle.com/) | 公开 |
| PCB-Component-Detection-CVM | BPCB | RGB | 元元件 | 9 | 101 | [Roboflow](https://roboflow.com/) | 公开 |
| DSLR | PCBA | RGB | 元件 | 4 | 748 | [TU Wien](https://tuwien.ac.at/) | 公开 |
| PCB-Vision | PCBA | RGB | 元件 | 4 | 106 | [GitHub](https://github.com/) | 公开 |
| Lite-On Dataset | PCBA | AOI | 混合 | 8 | 12200 | 私有 | 不可访问 |
| PCB-METAL | PCBA | RGB | 元件 | 4 | 3773 | 私有 | 不可访问 |
| PCB-MO | PCBA | RGB | 元件 | 6 | 19029 | 私有 | 不可访问 |
| PCB-SDD | PCBA | RGB | 元件 | 4 | 984 | 私有 | 不可访问 |
| PCB-MHS | PCBA | RGB | 元件 | 4 | 748 | 私有 | 不可访问 |
| AXI PCB defect detection | PCBA | AXI | 混合 | 4 | 32377 | 私有 | 不可访问 |

---

## 📊 UniPCB 数据统计

### 场景分布

| 场景 | 标注类型 | 占比 |
|------|---------|------|
| 完全标注 | 43% | 标注类别和边界框 |
| 弱标注 | 29% | 仅边界框标注 |
| 无标注 | 28% | 无标注，需模型检测 |

### 任务类型分布

| 任务类型 | 占比 |
|---------|------|
| 缺陷分析 | 13.1% |
| 缺陷详细描述 | 13.1% |
| 缺陷坐标 | 4.1% |
| 缺陷计数 | 7.6% |
| 缺陷分类 | 3.5% |
| 缺陷检测 | 3.5% |
| 缺陷定位 | 5.1% |
| 元件分析 | 11.6% |
| 元件描述 | 11.6% |
| 元件坐标 | 8.6% |
| 元件定位 | 3.4% |
| 元件计数 | 3.4% |
| 元件类型 | 3.4% |
| 目标描述 | 7.4% |

---

## 📋 数据格式

### 缺陷分类（13 类）

| 类别 | 说明 | 影响/功能 |
|------|------|---------|
| 结构 | 焊板对位错误、焊盘错位 | 导致开路、短路 |
| 焊盘偏移 | 钻孔与焊盘不对齐 | 影响连接、插入；可能导致开路 |
| 裂缝 | 基板或组件应力开裂 | 传播到开路；降低可靠性 |
| 物理损坏 | 开裂或碎裂 | 损害完整性；开路或短路 |
| 缺孔 | 需钻未完成 | 导致电气开路 |
| 缺焊盘 | 焊盘缺失；蚀刻或附着力差 | 阻止附着力；导致开路 |
| 老鼠咬 | 沿导线边缘的半圆形凹陷 | 降低承载能力；开路风险 |
| 尖刺 | 从导线边缘突出的铜 | 桥接间隙；短路风险 |
| 冷焊 | 发灰、粗糙表面；加热不足 | 高电阻；间歇性电气接触 |
| 焊料过多 | 凸起的焊点超出焊盘 | 短路风险；掩盖湿润问题 |
| 少锡 | 锡锡体积低；焊料不足 | 接头弱；间歇性或开路 |
| 焊盘腐蚀 | 氧化表面（储存不良） | 脱焊；接触不良或开路 |
| 焊桥 | 相邻焊盘之间意外连接 | 短路；器件烧毁风险 |
| 元件相关 | 连接器损坏、引脚损坏 | 中断电源/信号；不稳定通信 |
| 断开 | 导线、焊盘或焊点不连续 | 中断信号；导致失效或故障 |
| 短路 | 隔离导体间意外连接 | 高电流；器件烧毁或失效 |
| 假焊 | 孤在非预期区域 | 短路、寄生耦合、电磁干扰 |
| 机械 | 铜盘或焊盘上的磨痕 | 暴露金属；开路风险、干扰 |
| 污染 | 焊剂残留、油、指纹 | 导致泄漏、腐蚀或焊锡湿润不良 |
| 异物 | 尘土、金属芯片或碎片 | 短路、腐蚀；降低可靠性 |

### 元件分类（6 类）

| 类别 | 说明 | 功能 |
|------|------|------|
| 控制计算 | 微芯片、微控制器 | 核心逻辑；失效禁用主要功能 |
| 互连 | 连接器、插件 | 传输电源/信号；断开导致故障 |
| 无源 | 电容器、电感器 | 存储、滤波、耦合或去耦；失效导致噪声或重置 |
| 有源 | 二极管、晶体管 | 开关或放大；失效风险电路损坏 |
| 显示交互 | LED、LCD | 显示模块；用户界面；失效影响数据显示 |
| 电源保护 | 电池、保险丝 | 板载能源源；失效导致关机或数据丢失 |

---

## 🔄 数据流程

1. **数据收集**：从公开来源收集 PCB 数据
2. **预处理**：去重、过滤、规范化
3. **标注标准化**：统一分类系统
4. **训练集构建**：三阶段课程学习数据
5. **基准集构建**：多场景评估数据

详见论文附录和数据管道说明。
