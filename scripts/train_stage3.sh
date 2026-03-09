#!/bin/bash
# Stage 3 Training Script - Reinforcement Learning (RLHF/GRPO)
# Part of progressive curriculum learning pipeline

# Activate conda environment (adjust as needed)
# source /opt/conda/etc/profile.d/conda.sh
# con activate YOUR_ENV

export PYTHONPATH=PATH_TO_VERL:$PYTHONPATH
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export CUDA_LAUNCH_BLOCKING=1
export HYDRA_FULL_ERROR=1

# Set your wandb API key here (use environment variable in production)
# export WANDB_API_KEY="YOUR_WANDB_API_KEY"

export IOU_THR=0.30  # IoU threshold
export VERL_SAMPLE_LOG=OUTPUT_DIR/logs/log_answer.jsonl
export VERL_SAMPLE_LOG_EVERY=10
export PRIOR_JSON=DATA_PATH/train_prior_knowledge.json

# Choose engine: vllm or native
ENGINE=${1:-vllm}

# If using vllm<=0.6.3, set this to avoid bugs
export VLLM_ATTENTION_BACKEND=XFORMERS

python3 -m verl.trainer.main_ppo \
    algorithm.adv_estimator=grpo \
    data.train_files=DATA_PATH/stage3_train.parquet \
    data.val_files=DATA_PATH/stage3_test.parquet \
    data.train_batch_size=8 \
    data.max_prompt_length=4096 \
    data.max_response_length=512 \
    data.filter_overlong_prompts=True \
    data.truncation='error' \
    data.image_key=images \
    actor_rollout_ref.model.path=OUTPUT_DIR/stage2/checkpoint-LAST-merged \
    actor_rollout_ref.actor.optim.lr=2e-6 \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.ppo_mini_batch_size=8 \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.model.lora_rank=64 \
    actor_rollout_ref.model.lora_alpha=128 \
    actor_rollout_ref.model.target_modules=all-linear \
    actor_rollout_ref.model.exclude_modules='.*visual.*' \
    actor_rollout_ref.actor.use_kl_loss=True \
    actor_rollout_ref.actor.kl_loss_coef=0.01 \
    actor_rollout_ref.actor.kl_loss_type=low_var_kl \
    actor_rollout_ref.actor.entropy_coeff=0 \
    actor_rollout_ref.actor.strategy=fsdp \
    actor_rollout_ref.actor.fsdp_config.fsdp_size=-1 \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.use_orig_params=False \
    actor_rollout_ref.actor.fsdp_config.param_offload=False \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=False \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.rollout.tensor_model_parallel_size=1 \
    actor_rollout_ref.rollout.dtype=bfloat16 \
    actor_rollout_ref.rollout.name=$ENGINE \
    actor_rollout_ref.rollout.load_format="safetensors" \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.7 \
    actor_rollout_ref.rollout.n=8 \
    actor_rollout_ref.actor.entropy_checkpointing=True \
    actor_rollout_ref.rollout.max_num_seqs=8 \
    actor_rollout_ref.rollout.layered_summon=True \
    actor_rollout_ref.model.use_shm=True \
    actor_rollout_ref.rollout.max_num_batched_tokens=12288 \
    actor_rollout_ref.ref.fsdp_config.param_offload=False \
    actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=1 \
    algorithm.use_kl_in_reward=False \
    trainer.critic_warmup=0 \
    trainer.logger='["console","wandb"]' \
    trainer.project_name="unipcb-stage3" \
    trainer.experiment_name="stage3_grpo" \
    custom_reward_function.path=scripts/train_stage2/reward_function.py \
    custom_reward_function.name=compute_score \
    trainer.nnodes=1 \
    trainer.n_gpus_per_node=8 \
    trainer.save_freq=50 \
    trainer.test_freq=10 \
    actor_rollout_ref.rollout.enable_chunked_prefill=False \
    trainer.default_local_dir=OUTPUT_DIR/stage3 \
    trainer.total_epochs=2
