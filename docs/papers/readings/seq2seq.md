# Sequence to Sequence Learning with Neural Networks

## Citation

Sutskever et al.. *Sequence to Sequence Learning with Neural Networks.* 2014. [https://arxiv.org/abs/1409.3215](https://arxiv.org/abs/1409.3215)

## One-sentence contribution

Encoder–decoder LSTM architecture for variable-length input/output mapping.

## Problem

Mapping variable-length input sequences to variable-length outputs—machine translation, summarization, dialogue—required models that could read an entire source and generate a target of different length token by token.

## Prior art

Phrase-based statistical MT (Koehn et al.) dominated with hand-engineered features and separate language/translation models. Earlier neural attempts used fixed-size windows or bag-of-words encodings that could not preserve word order or long dependencies.

## Core idea

Sutskever et al. stacked two LSTMs: an encoder reads the input sequence and produces a fixed-size context vector from its final hidden state; a decoder LSTM generates the output sequence conditioned on that vector. Reversing the source sentence improved performance by placing words near the context boundary that align with early target tokens. Deep LSTMs (4 layers) with careful initialization and dropout regularization made the architecture trainable on large parallel corpora.

## Evidence

- WMT'14 English→French: BLEU 34.8, beating the best statistical MT system (33.3) on the same data by a significant margin.
- Qualitative attention to the context vector showed the model learned meaningful source-target alignments without explicit alignment supervision.
- Ensemble of 5 models with beam search (width 2) and length normalization further improved results.
- Reversing input sequences alone contributed ~1–2 BLEU points—an unusually simple architectural trick with large effect.

## Limitations

- The fixed-size context vector is a bottleneck for long inputs; information from early encoder tokens is compressed and often lost.
- Sequential encoding/decoding prevents parallelization during training and inference.
- Exposure bias during training (teacher forcing) causes error accumulation at decode time.
- Required large parallel corpora; low-resource language pairs remained difficult.

## Lasting impact

Established the encoder–decoder template that attention and Transformers extended. Every modern NMT, summarization, and speech-to-text system traces lineage to this two-LSTM design.

## Reproduction exercise

Train a 2-layer LSTM seq2seq on the small Multi30k German→English dataset (~30k pairs). Compare BLEU with and without source reversal. Use a single GPU for ~30 minutes. Inspect attention-free alignments by visualizing which encoder states the decoder hidden state is closest to at each step.

## Related chapters

- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)
- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)
- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)

## Related concepts

- [Seq2seq](../../concepts/cards/seq2seq.md)
- [Lstms](../../concepts/cards/lstms.md)
- [Sampling](../../concepts/cards/sampling.md)
