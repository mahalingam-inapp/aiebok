# FlashAttention: Fast and Memory-Efficient Exact Attention

## Citation

Dao et al.. *FlashAttention: Fast and Memory-Efficient Exact Attention.* 2022. [https://arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135)

## One-sentence contribution

IO-aware attention algorithm reduces memory and speeds training/inference.

## Problem

Standard attention implementation materializes the full N×N attention matrix in GPU HBM (high-bandwidth memory), making attention memory-bound rather than compute-bound. Long sequences (4k+ tokens) exhaust GPU memory during training.

## Prior art

Gradient checkpointing traded compute for memory. Sparse/linear attention approximations reduced memory but changed the computation. Kernel fusion attempts (xformers predecessors) had limited adoption.

## Core idea

Dao et al. restructured attention computation to minimize HBM reads/writes using tiling: load blocks of Q, K, V into fast SRAM, compute attention scores and weighted values incrementally, and never materialize the full N×N matrix. The algorithm is IO-aware—analyzing memory hierarchy (SRAM vs. HBM) to minimize data movement. FlashAttention produces exact attention (not an approximation) with different memory access patterns. FlashAttention-2 further optimized work partitioning and warp scheduling.

## Evidence

- 2–4× training speedup on GPT-2 and BERT vs. standard PyTorch attention.
- Enabled 2× longer sequences on the same GPU memory budget.
- End-to-end BERT training 15% faster; GPT-2 training 3× faster at sequence length 1K.
- Exact attention—no quality difference vs. standard implementation.

## Limitations

- CUDA-specific implementation; AMD/TPU require separate ports.
- Head dimension constraints (typically ≤128) for optimal performance.
- Integration requires compatible model code (now standard in PyTorch 2.0+, HuggingFace).
- Does not reduce O(n²) compute—only memory and constant factors.

## Lasting impact

FlashAttention is the default attention implementation in PyTorch 2.0, HuggingFace Transformers, and every major training framework. It enabled the long-context models (32k, 128k tokens) that define the current generation.

## Reproduction exercise

Benchmark attention on sequence lengths 512, 2048, 8192 using standard PyTorch vs. `flash_attn` on the same GPU. Measure peak memory and wall-clock time. Verify outputs are numerically identical (within fp16 tolerance).

## Related chapters

- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)
- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)

## Related concepts

- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Long Context](../../concepts/cards/long-context.md)
- [Gpus](../../concepts/cards/gpus.md)
