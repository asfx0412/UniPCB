# 训练指南

本文档介绍如何训练 PCB-GPT 模型。

---

## 三阶段渐进式课程学习

PCB-GPT 采用三阶段训练策略，模仿人类专家的学习过程：

### 阶段 1：基础元件识别
- **目标**：学习基本的 PCB 元件识别
- **数据**：简单场景，单一元件
- **任务**：分类和基础检测
- **脚本**：`scripts/train_stage1.sh`

### 阶段 2：缺陷检测
- **目标**：学习缺陷模式识别
- **数据**：包含常见缺陷的样本
- **任务**：缺陷检测和定位
- **脚本**：`scripts/train_stage2.sh`

### 阶段 3：强化学习
- **目标**：学习复杂场景推理和优化
- **数据**：真实工业场景
- **任务**：综合质量分析
- **脚本**：`scripts/train_stage3.sh`

---

## 使用方法

### 准备工作

1. **下载基础模型**
```bash
# 下载 Qwen2.5-VL-7B-Instruct
# 设置环境变量 BASE_MODEL_PATH 指向模型路径
```

2. **准备训练数据**
```bash
# 将数据集放在 DATA_PATH 目录下
# 确保包含三个阶段的数据文件
```

3. **配置路径**
编辑训练脚本，替换以下占位符：
- `BASE_MODEL_PATH`: 基础模型路径
- `DATA_PATH`: 数据路径
- `OUTPUT_DIR`: 输出路径
- `YOUR_NAME`: 作者名

### 阶段 1 训练

```bash
cd UniPCB
bash scripts/train_stage1.sh
```

训练完成后，LoRA 权重保存在 `output/stage1/` 目录下。

### 阶段 2 训练

在阶段 1 完成后运行：

```bash
bash scripts/train_stage2.sh
```

训练完成后，LoRA 权重保存在 `output/stage2/` 目录下。

### 阶段 3 训练（强化学习）

阶段 3 使用 PPO/GRPO 算法进行强化学习：

```bash
# 1. 安装依赖
conda activate YOUR_ENV
pip install verl

# 2. 运行训练
bash scripts/train_stage3.sh
```

---

## 推理和模型合并

### 合并 LoRA 权重

```bash
bash scripts/infer_merge.sh
```

这会将 LoRA 权重与基础模型合并，生成完整的模型文件。

### 运行推理

```bash
python scripts/infer_unified.py \
    --model qwen \
    --data path/to/test_data.json \
    --output results/predictions.json \
    --api-base YOUR_API_ENDPOINT
```

---

## 配置说明

### 阶段 1 & 2 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `learning_rate` | 学习率 | 1e-4 |
| `lora_rank` | LoRA 秩 | 64 |
| `lora_alpha` | LoRA alpha | 128 |
| `gradient_accumulation_steps` | 梯度累积步数 | 8 |
| `max_pixels` | 最大像素数 | 3000000 |
| `max_length` | 最大序列长度 | 10240 |

### 阶段 3 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
(以下为阶段 3 特有参数，按需求配置)
| `learning_rate` | 学习率 | 2e-6 |
| `train_batch_size` | 训练批次大小 | 8 |
| `max_prompt_length` | 最大提示长度 | 4096 |
| `max_response_length` | 最大响应长度 | 512 |
| `IOU_THR` | IoU 阈值 | 0.30 |
| `WT` | 准确率权重 | 0.9 |
| `WF` | 格式权重 | 0.1 |

---

## 常见问题

### Q1: GPU 内存不足

A: 减少批次大小或使用梯度检查点：
```bash
--per_device_train_batch_size 1
--gradient_accumulation_steps 16
```

### Q2: 训练速度慢

A: 增加工作线程或使用分布式训练：
```bash
--dataloader_num_workers 4
```

### Q3: 强化学习不稳定

A: 调整学习率和 KL 散度系数：
```bash
actor_rollout_ref.actor.optim.lr=1e-6
actor_rollout_ref.actor.kl_loss_coef=0.02
```

---

## 许可证

训练脚本和数据使用 MIT 许可证。请确保遵守基础模型的许可证。
