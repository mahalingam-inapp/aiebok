# RoFormer: Enhanced Transformer with Rotary Position Embedding

## Citation

Su et al.. *RoFormer: Enhanced Transformer with Rotary Position Embedding.* 2021. [https://arxiv.org/abs/2104.09864](https://arxiv.org/abs/2104.09864)

## One-sentence contribution

Rotary embeddings encode relative position in attention.

## Problem

Transformers need position information but fixed absolute embeddings generalize poorly to longer sequences.

## Prior art

Sinusoidal and learned absolute positional embeddings dominated early transformers.

## Core idea

Rotary Position Embedding (RoPE) encodes relative position by rotating query and key vectors in complex space as a function of token index.

## Evidence

- Widely adopted in LLaMA, GPT-NeoX, and many open models.
- Improved length extrapolation versus absolute embeddings in several studies.

## Limitations

- Extrapolation beyond train length still degrades
- Implementation details affect stability

## Lasting impact

De facto standard positional scheme for decoder-only LLMs.

## Reproduction exercise

Plot attention distance bias with and without RoPE on a toy transformer; compare perplexity on longer sequences.

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)

## Related concepts

- [Position](../../concepts/cards/position.md)
- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Long Context](../../concepts/cards/long-context.md)
