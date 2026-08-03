# Mistral 7B

## Citation

Jiang et al.. *Mistral 7B.* 2023. [https://arxiv.org/abs/2310.06825](https://arxiv.org/abs/2310.06825)

## One-sentence contribution

Efficient open model with sliding-window attention.

## Problem

Open models needed strong quality at smaller sizes for efficient deployment.

## Prior art

Many open models prioritized scale over inference efficiency.

## Core idea

Mistral 7B combines grouped-query attention, sliding window attention, and careful training data to punch above its weight class.

## Evidence

- Competitive benchmark scores versus larger models at release.
- Widely adopted as an efficient open-weights baseline.

## Limitations

- Still requires safety tuning for product use
- Windowed attention affects very long contexts

## Lasting impact

Popularized efficient open models for production prototyping.

## Reproduction exercise

Benchmark Mistral-class 7B vs a 13B baseline on your task slice with equal latency budget.

## Related chapters

- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)
- [05 Deployment And Routing](../../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md)

## Related concepts

- [Open Weights](../../concepts/cards/open-weights.md)
- [Model Routing](../../concepts/cards/model-routing.md)
- [KV Cache](../../concepts/cards/kv-cache.md)
