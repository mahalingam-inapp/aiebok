# Mixtral of Experts

## Citation

Jiang et al.. *Mixtral of Experts.* 2024. [https://arxiv.org/abs/2401.04088](https://arxiv.org/abs/2401.04088)

## One-sentence contribution

Sparse MoE open model with strong quality/FLOP.

## Problem

Users wanted open models with higher quality without paying full dense-model inference costs.

## Prior art

Dense 70B-class models were expensive to serve; small dense models lacked quality.

## Core idea

Mixtral combines sparse MoE layers in an open model, activating few experts per token for better quality/FLOP.

## Evidence

- Strong benchmark performance versus larger dense open models at release.
- Public weights enabled local and hosted deployment patterns.

## Limitations

- MoE serving complexity
- Expert load imbalance can hurt latency

## Lasting impact

Made MoE practical in open-weights product discussions.

## Reproduction exercise

Profile tokens/sec for MoE vs dense model with same API on 100 prompts.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related concepts

- [Mixture Of Experts](../../concepts/cards/mixture-of-experts.md)
- [Model Routing](../../concepts/cards/model-routing.md)
- [Batching](../../concepts/cards/batching.md)
