# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

## Citation

Gu & Dao. *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* 2023. [https://arxiv.org/abs/2312.00752](https://arxiv.org/abs/2312.00752)

## One-sentence contribution

Selective SSMs offer recurrent-like efficiency with strong quality.

## Problem

Transformer self-attention scales O(n²) in sequence length, limiting context windows and making long-document processing expensive at both training and inference time. Linear-time alternatives were needed without sacrificing quality.

## Prior art

State space models (S4) achieved linear scaling but were time-invariant—treating all inputs uniformly. Linear attention variants (Performers, Linformer) approximated attention but often degraded quality. RWKV combined RNN and Transformer properties.

## Core idea

Gu & Dao introduced selective state space models (SSMs) where the SSM parameters (Δ, B, C) are input-dependent functions rather than fixed. This selectivity lets the model decide what to remember and what to ignore per token—addressing the weakness of prior SSMs on discrete language tasks. Mamba eliminates the SSM's time-invariance while maintaining O(n) compute and O(1) memory per step at inference. A hardware-aware parallel scan algorithm enables efficient training.

## Evidence

- Language modeling perplexity matched Transformers at scales up to 3B parameters on The Pile.
- 5× higher throughput than Transformers at sequence length 8192 during generation.
- Selective mechanism ablation: input-dependent Δ was the critical component vs. time-invariant S4.
- Mamba-2 further unified SSM and attention perspectives with improved constants.

## Limitations

- Ecosystem immaturity—fewer pre-trained checkpoints, tools, and fine-tuning recipes vs. Transformers.
- Hybrid Mamba-Transformer models often outperform pure Mamba on downstream tasks.
- CUDA kernel dependency for efficient training; CPU inference is slow.
- Long-range recall benchmarks (Needle in Haystack) show mixed results vs. full attention.

## Lasting impact

Mamba proved that attention is not strictly necessary for language modeling quality, opening a research frontier in alternative sequence architectures. Mamba-2 and hybrid models (Jamba) are actively deployed in production.

## Reproduction exercise

Train a tiny Mamba model (2 layers, d=256) on a character-level Shakespeare corpus using the `mamba-ssm` library. Compare training speed and perplexity against a Transformer of equal size at sequence lengths 512 and 2048.

## Related chapters

- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)
- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [05 Long Context World Models And Continual Learning](../../books/13-multimodal-and-frontier-systems/05-long-context-world-models-and-continual-learning.md)

## Related concepts

- [State Spaces](../../concepts/cards/state-spaces.md)
- [Long Context](../../concepts/cards/long-context.md)
- [Lstms](../../concepts/cards/lstms.md)
