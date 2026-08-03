# PaLM: Scaling Language Modeling with Pathways

## Citation

Chowdhery et al.. *PaLM: Scaling Language Modeling with Pathways.* 2022. [https://arxiv.org/abs/2204.02311](https://arxiv.org/abs/2204.02311)

## One-sentence contribution

Large-scale training with pathways and sparse MoE elements.

## Problem

Scaling language models while keeping inference efficient for serving.

## Prior art

Dense transformers scaled quality but multiplied FLOPs per token linearly with width.

## Core idea

PaLM uses a sparse mixture-of-experts transformer trained at scale with careful data and routing, improving quality per FLOP.

## Evidence

- Reported strong results on reasoning and code benchmarks at 540B scale.
- MoE routing activates a subset of experts per token.

## Limitations

- Serving MoE at scale is operationally complex
- Reproduction cost is prohibitive for most teams

## Lasting impact

Influenced large-scale training recipes and MoE serving research.

## Reproduction exercise

Study a public MoE model card and estimate active parameters vs total; run tiny MoE tutorial model if available.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related concepts

- [Mixture Of Experts](../../concepts/cards/mixture-of-experts.md)
- [Scaling Laws](../../concepts/cards/scaling-laws.md)
- [Batching](../../concepts/cards/batching.md)
