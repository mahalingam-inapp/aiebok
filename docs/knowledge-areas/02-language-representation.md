# KA 02 — Language & Representation

## Purpose

Make language computable for search and models.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Why Language Is Hard** — read [chapter](../books/03-language-and-representation/01-why-language-is-hard.md), run [lab](../labs/0301-why-language-is-hard.md), lesson page [L-02-language-representation-01](../lessons/02-language-representation-01.md)
2. **Corpora and Text Pipelines** — read [chapter](../books/03-language-and-representation/02-corpora-and-text-pipelines.md), run [lab](../labs/0302-corpora-and-text-pipelines.md), lesson page [L-02-language-representation-02](../lessons/02-language-representation-02.md)
3. **Tokenization** — read [chapter](../books/03-language-and-representation/03-tokenization.md), run [lab](../labs/0303-tokenization.md), lesson page [L-02-language-representation-03](../lessons/02-language-representation-03.md)
4. **From Sparse Features to Embeddings** — read [chapter](../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md), run [lab](../labs/0304-from-sparse-features-to-embeddings.md), lesson page [L-02-language-representation-04](../lessons/02-language-representation-04.md)
5. **Similarity and Vector Search** — read [chapter](../books/03-language-and-representation/05-similarity-and-vector-search.md), run [lab](../labs/0305-similarity-and-vector-search.md), lesson page [L-02-language-representation-05](../lessons/02-language-representation-05.md)
6. **Embedding Systems in Production** — read [chapter](../books/03-language-and-representation/06-embedding-systems-in-production.md), run [lab](../labs/0306-embedding-systems-in-production.md), lesson page [L-02-language-representation-06](../lessons/02-language-representation-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Why Language Is Hard | Language is not a string-processing problem; it is communication under context and assumpt | Apply without baseline or slice eval |
| Corpora and Text Pipelines | Representation quality cannot recover information destroyed during ingestion. | Apply without baseline or slice eval |
| Tokenization | Tokenization is an engineering boundary that determines what units the model can efficient | Apply without baseline or slice eval |
| From Sparse Features to Embeddings | Different representations preserve different relationships; no representation is universal | Apply without baseline or slice eval |

## Core topics

- [BM25](../concepts/cards/bm25.md)
- [word embeddings](../concepts/cards/word-embeddings.md)
- [ANN indexes](../concepts/cards/ann-indexes.md)

## Guided resources

- Primary book: [Language and Representation](../books/03-language-and-representation/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Build lexical and semantic search baselines.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
