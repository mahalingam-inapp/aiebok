# Efficient Estimation of Word Representations in Vector Space

## Citation

Mikolov et al.. *Efficient Estimation of Word Representations in Vector Space.* 2013. [https://arxiv.org/abs/1301.3781](https://arxiv.org/abs/1301.3781)

## One-sentence contribution

Introduced skip-gram and CBOW dense word vectors learned from co-occurrence.

## Problem

Classical NLP represented words as sparse one-hot vectors with no notion of semantic similarity—'cat' and 'dog' were as distant as 'cat' and 'finance.' The field needed dense, trainable word representations that capture distributional meaning from unlabeled text.

## Prior art

Matrix factorization on co-occurrence counts (LSA, HAL) produced vectors but scaled poorly and treated all co-occurrences equally. Earlier neural language models (Collobert & Weston, word2vec predecessors) showed promise but trained too slowly for web-scale corpora.

## Core idea

Mikolov et al. proposed two shallow architectures—CBOW predicts a word from surrounding context; skip-gram predicts context from a center word. Negative sampling replaces the full softmax with a small set of contrastive noise draws, making training tractable on billions of tokens. Hierarchical softmax offers an alternative speedup via a binary tree over the vocabulary. The result is a single dense vector per word type, learned entirely from local co-occurrence statistics without labeled data.

## Evidence

- Semantic and syntactic word-analogy benchmark: skip-gram with negative sampling scored ~70% on the Google analogy set (king−man+woman≈queen).
- Trained on Google News (~100B tokens); nearest-neighbor inspection shows coherent semantic clusters (countries, professions, verb tenses).
- Downstream NER and sentiment tasks improved when word2vec vectors replaced one-hot or random initialization.
- Skip-gram outperformed CBOW on rare words; CBOW was faster to train on frequent tokens.

## Limitations

- One vector per word type—polysemy ('bank' river vs. financial) is collapsed into a single point.
- No subword handling; out-of-vocabulary words require fallback to UNK or character models.
- Static embeddings do not adapt to sentence-level context (addressed later by ELMo, BERT).
- Training data bias (e.g., gender stereotypes in analogies) propagates directly into geometry.

## Lasting impact

word2vec made distributional semantics practical at scale and became the default initialization for neural NLP through 2016–2018. The skip-gram + negative sampling recipe survives in modern embedding APIs and as a pedagogical baseline for representation learning.

## Reproduction exercise

Download a 100 MB Wikipedia dump, tokenize, and train skip-gram (vector size 300, window 5, 5 negative samples) using Gensim or fastText. Evaluate on a 50-item analogy subset (capital cities, gender pairs). Compare against random vectors to confirm the geometry is non-trivial. Budget: one CPU hour.

## Related chapters

- [04 From Sparse Features To Embeddings](../../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md)
- [05 Similarity And Vector Search](../../books/03-language-and-representation/05-similarity-and-vector-search.md)
- [03 Unsupervised And Representation Learning](../../books/02-machine-learning-systems/03-unsupervised-and-representation-learning.md)

## Related concepts

- [Word Embeddings](../../concepts/cards/word-embeddings.md)
- [Representation Learning](../../concepts/cards/representation-learning.md)
- [N Grams](../../concepts/cards/n-grams.md)
