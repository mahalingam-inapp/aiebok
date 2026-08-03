# Attention Is All You Need

## Citation

Vaswani et al.. *Attention Is All You Need.* 2017. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## One-sentence contribution

Self-attention transformer replaced recurrence for sequence modeling.

## Problem

Recurrent and convolutional sequence models process tokens sequentially, limiting training parallelization and making long-range dependency learning depend on many propagation steps through time.

## Prior art

LSTM/GRU seq2seq with attention dominated NMT but required O(n) sequential steps. ConvS2S and ByteNet used convolutions for partial parallelization but still scaled path length with distance. No architecture had removed recurrence entirely while matching RNN quality.

## Core idea

Vaswani et al. replaced recurrence with multi-head self-attention: each token attends to all others in the same layer, computing relevance via scaled dot-product scores. Positional encodings (sinusoidal or learned) inject order information since attention is permutation-invariant. Encoder and decoder stacks alternate self-attention, cross-attention (decoder→encoder), and position-wise feed-forward layers with residual connections and layer normalization. The design enables full parallelization over sequence length during training.

## Evidence

- WMT'14 English→German: 28.4 BLEU—new state of the art, training in 3.5 days on 8 P100 GPUs vs. best published RNN results.
- English→French: 41.8 BLEU (single model, no ensemble)—large margin over prior work.
- Attention head analysis showed heads specialize (syntax, anaphora, positional).
- Training cost scaled better with sequence length than LSTM baselines due to parallelism.

## Limitations

- Self-attention memory and compute scale O(n²) with sequence length—prohibitive for very long documents without modifications.
- Positional encodings are weaker than explicit recurrence for some extrapolation tasks (length generalization).
- Requires large training data and careful warmup/regularization; small-data regimes favor pre-trained models over training from scratch.
- Cross-attention in the decoder still creates an encoder-decoder asymmetry that later decoder-only models (GPT) removed.

## Lasting impact

The Transformer became the universal backbone for language, vision, speech, and multimodal models. BERT, GPT, T5, ViT, and Whisper all inherit this block structure. 'Attention is all you need' accurately predicted a decade of architecture design.

## Reproduction exercise

Implement a tiny Transformer (2 layers, 4 heads, d_model=128) on a copy task (reverse or duplicate sequences of length 10–20). Verify it converges where a bag-of-words baseline fails. Then fine-tune a HuggingFace 'tiny-random' Transformer on SST-2 sentiment to observe transfer from pre-trained weights vs. random init.

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)
- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)
- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)

## Related concepts

- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Position](../../concepts/cards/position.md)
- [Residual Connections](../../concepts/cards/residual-connections.md)
