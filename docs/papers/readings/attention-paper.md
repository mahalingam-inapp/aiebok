# Neural Machine Translation by Jointly Learning to Align and Translate

## Citation

Bahdanau et al.. *Neural Machine Translation by Jointly Learning to Align and Translate.* 2015. [https://arxiv.org/abs/1409.0473](https://arxiv.org/abs/1409.0473)

## One-sentence contribution

Additive attention let decoders focus on relevant encoder states.

## Problem

The seq2seq context vector bottleneck forced the decoder to reconstruct the entire source meaning from a single fixed-size vector, hurting translation quality on long sentences and making alignments opaque.

## Prior art

Sutskever seq2seq used only the encoder's last hidden state. Earlier alignment models in statistical MT computed explicit source-target word alignments but were not differentiably integrated into neural decoders.

## Core idea

Bahdanau et al. introduced additive (concat) attention: at each decode step the decoder computes an alignment score between its current state and every encoder hidden state, softmax-normalizes into weights, and forms a context vector as the weighted sum of encoder outputs. This lets the decoder focus on different source positions per target word—effectively learning a soft alignment. The attention context replaces the single fixed vector as the conditioning signal for each output token.

## Evidence

- WMT'14 English→French: BLEU 28.45 (attention) vs. 26.75 (no attention) on the same architecture—roughly 6% relative gain from attention alone.
- Attention weight heatmaps visually match intuitive word alignments (e.g., English 'zone' → French 'zone').
- Performance degradation on long sentences was substantially reduced compared to fixed-context seq2seq.
- Joint training of alignment and translation avoided the pipeline errors of statistical MT.

## Limitations

- Attention over all encoder states is O(n·m) in source and target length—expensive for very long documents.
- Still built on sequential RNNs; cannot parallelize encoder/decoder passes.
- Alignment weights are not guaranteed to be interpretable or sparse in all cases.
- Does not address the exposure bias or beam search approximation problems.

## Lasting impact

Attention became the standard conditioning mechanism for sequence models and the direct precursor to self-attention in Transformers. The idea that models should dynamically select relevant context per step is now universal in NLP and vision.

## Reproduction exercise

Implement additive attention on top of a seq2seq baseline (same Multi30k setup). Plot attention heatmaps for 10 held-out sentence pairs. Measure BLEU delta with and without attention on sentences binned by source length (short vs. long). Expect the long-sentence bin to show the largest gain.

## Related chapters

- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)
- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)
- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)

## Related concepts

- [Scaled Dot Product](../../concepts/cards/scaled-dot-product.md)
- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Seq2seq](../../concepts/cards/seq2seq.md)
