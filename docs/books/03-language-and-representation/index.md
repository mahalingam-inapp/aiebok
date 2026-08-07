# Book 3 — Language and Representation

## Purpose

Understand how language becomes computable representations and why embeddings enable semantic systems.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Why Language Is Hard__

    Explore ambiguity, reference, syntax, semantics, pragmatics, intent, and the dependence of meaning on context…

    [Open chapter →](01-why-language-is-hard.md)

-   :material-numeric-2-circle:{ .lg .middle } __Corpora and Text Pipelines__

    Learn how collection, encoding, normalization, language detection, segmentation, privacy, and provenance shap…

    [Open chapter →](02-corpora-and-text-pipelines.md)

-   :material-numeric-3-circle:{ .lg .middle } __Tokenization__

    Understand character, word, and subword tokenization; BPE, WordPiece, and SentencePiece; and the impact on co…

    [Open chapter →](03-tokenization.md)

-   :material-numeric-4-circle:{ .lg .middle } __From Sparse Features to Embeddings__

    Move from one-hot vectors, n-grams, TF–IDF, and BM25 to learned dense representations.

    [Open chapter →](04-from-sparse-features-to-embeddings.md)

-   :material-numeric-5-circle:{ .lg .middle } __Similarity and Vector Search__

    Connect distance metrics, normalization, nearest neighbors, approximate indexes, clustering, filtering, and r…

    [Open chapter →](05-similarity-and-vector-search.md)

-   :material-numeric-6-circle:{ .lg .middle } __Embedding Systems in Production__

    Select and evaluate embedding models, manage versions and re-indexing, protect tenant boundaries, and monitor…

    [Open chapter →](06-embedding-systems-in-production.md)

</div>

## Entry prerequisites

- Books 1–2
- Vectors and dot products
- Basic text processing

## Book project

Build and evaluate a multilingual semantic search engine with lexical and vector baselines.

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Manning, Raghavan & Schütze — Introduction to Information Retrieval
- Mikolov et al. — Efficient Estimation of Word Representations in Vector Space

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
