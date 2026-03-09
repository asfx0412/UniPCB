#!/bin/bash
# Stage 1 Training Script - Basic Component Recognition
# Part of progressive curriculum learning pipeline

# GPU Configuration (adjust based on your setup)
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
CUDA_LAUNCH_BLOCKING=1 \
MAX_PIXELS=3000000 \
swift sft \
    --model BASE_MODEL_PATH \
    --train_type lora \
    --dataset 'DATA_PATH/stage1_cn.json' \
              'DATA_PATH/stage1_en.json' \
              'DATA_PATH/stage1_general.json' \
    --num_train_epochs 1 \
    --target_modules 'q_proj', 'v_proj' \
    --dataloader_num_workers 1 \
    --dataloader_persistent_workers False \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --lora_rank 64 \
    --lora_alpha 128 \
    --gradient_accumulation_steps 8 \
    --eval_steps 1000 \
    --max_pixels 3000000 \
    --save_steps 2000 \
    --save_total_limit 2 \
    --logging_steps 500 \
    --max_length 10240 \
    --output_dir output/stage1 \
    --system 'You are a helpful assistant specializing in PCB analysis.' \
    --warmup_ratio 0.05 \
    --model_author YOUR_NAME \
    --model_name unipcb-stage1 \
