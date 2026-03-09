#!/bin/bash
# Inference and Model Merge Script
# Merges LoRA weights with base model for inference

# GPU Configuration
CUDA_VISIBLE_DEVICES=0 \
MAX_PIXELS=3000000 \
swift infer \
    --ckpt_dir OUTPUT_DIR/stage2/checkpoint-LAST \
    --load_dataset_config true \
    --merge_lora true \
    --output_dir OUTPUT_DIR/merged_model
