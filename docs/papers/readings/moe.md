# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

## Citation

Shazeer et al.. *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* 2017. [https://arxiv.org/abs/1701.06538](https://arxiv.org/abs/1701.06538)

## One-sentence contribution

Conditional computation activates subsets of experts per token.

## Problem

Dense Transformer FFN layers activate all parameters for every token—scaling model capacity linearly increases compute per token. Conditional computation could activate only relevant subsets of parameters per input.

## Prior art

Mixture of Experts literature (Jordan & Jacobs, 1994) existed but was hard to train at scale. GShard and Switch Transformer later simplified MoE for Transformers. Ensemble methods increased capacity but multiplied compute.

## Core idea

Shazeer et al. introduced a Sparsely-Gated Mixture-of-Experts layer: replace the single FFN with N expert FFNs and a gating network that outputs a sparse weight vector per token. Each token activates only the top-k experts (typically k=1–2). A load-balancing auxiliary loss prevents collapse to a single expert. Total parameters scale with N, but compute per token scales with k—decoupling capacity from FLOPs.

## Evidence

- 137B MoE with 128 experts matched dense model quality on LM benchmark with ~10× less compute per token (k=2 of 128).
- 1T parameter model with sparse activation trained successfully on Google infrastructure.
- Load-balancing loss was essential—without it, gating collapsed to 1–2 experts.
- MoE layers added at every other Transformer block balanced quality and routing overhead.

## Limitations

- Expert parallelism requires complex distributed training (all-to-all communication).
- Load imbalance causes some GPUs to idle while others are saturated.
- Routing instability during training—expert assignment shifts across checkpoints.
- Inference serving is harder: experts may reside on different devices, adding latency.

## Lasting impact

MoE became the architecture behind Mixtral, GPT-4 (rumored), and Google's Switch Transformer. It enables trillion-parameter models with manageable inference cost and is the primary scaling path beyond dense Transformers.

## Reproduction exercise

Implement a 4-expert MoE FFN layer (top-1 routing) in a small Transformer using PyTorch. Train on a character-level LM task and compare perplexity against a dense FFN of equal total parameters. Monitor expert utilization histograms to verify load balancing.

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)
- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)

## Related concepts

- [Mixture Of Experts](../../concepts/cards/mixture-of-experts.md)
- [Routing](../../concepts/cards/routing.md)
- [Batching](../../concepts/cards/batching.md)
