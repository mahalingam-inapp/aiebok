# Deep contextualized word representations (ELMo)

## Citation

Peters et al.. *Deep contextualized word representations (ELMo).* 2018. [https://arxiv.org/abs/1802.05365](https://arxiv.org/abs/1802.05365)

## One-sentence contribution

Contextual embeddings from biLM layers improve downstream NLP.

## Problem

Context-independent word vectors could not handle polysemy or sentence-level meaning.

## Prior art

word2vec and GloVe assigned one vector per word type regardless of surrounding context.

## Core idea

ELMo runs deep bi-directional LSTM language models and concatenates layer representations to produce contextual embeddings for each token occurrence.

## Evidence

- Large improvements on SNLI, SQuAD, and NER versus static embeddings.
- Lower layers capture syntax; upper layers capture semantics in probing analyses.

## Limitations

- Slow inference vs. transformers
- Heavy compared to fine-tuning BERT once

## Lasting impact

Popularized contextual representations and set the stage for BERT-style pretraining.

## Reproduction exercise

Fine-tune a small ELMo-style model on SST-2 via HuggingFace ELMo checkpoints if available, or compare static vs contextual embeddings on NER.

## Related chapters

- [04 From Sparse Features To Embeddings](../../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md)
- [01 Sequence Models Before Transformers](../../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md)

## Related concepts

- [Word Embeddings](../../concepts/cards/word-embeddings.md)
- [Representation Learning](../../concepts/cards/representation-learning.md)
- [Lstms](../../concepts/cards/lstms.md)
