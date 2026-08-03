# GQA: Training Generalized Multi-Query Transformer Models

## Citation

Ainslie et al.. *GQA: Training Generalized Multi-Query Transformer Models.* 2023. [https://arxiv.org/abs/2305.13245](https://arxiv.org/abs/2305.13245)

## One-sentence contribution

Grouped-query attention reduces KV cache footprint.

## Problem

Multi-head attention KV cache memory grows with heads, limiting long-context batch size.

## Prior art

Standard MHA stores separate K/V per head for each token.

## Core idea

Grouped-query attention shares K/V heads among query head groups, shrinking KV cache with modest quality impact.

## Evidence

- Used in several efficient open models; reported near-MHA quality with lower memory bandwidth.
- Enables larger batch or longer context on same GPU memory.

## Limitations

- Not identical to MHA quality on all tasks
- Requires kernel support for best speedups

## Lasting impact

Common optimization in modern inference stacks alongside GQA/MLA variants.

## Reproduction exercise

Compare peak memory during decode for MHA vs GQA config in a small transformer implementation or framework flags.

## Related chapters

- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related concepts

- [KV Cache](../../concepts/cards/kv-cache.md)
- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Batching](../../concepts/cards/batching.md)
