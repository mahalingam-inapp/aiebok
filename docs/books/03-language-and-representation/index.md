# Language and Representation

Technical course 03 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Understand how language becomes computable representations and why embeddings enable semantic systems.

[Start the first lecture](01-why-language-is-hard.md){ .md-button .md-button--primary .study-start data-course="03-language-and-representation" }
[Download the course notebook](../../assets/notebooks/03-language-and-representation.ipynb){ .md-button download }

## Practice case · The library card that goes by three names

Marisol runs a library’s multilingual help desk. Patrons call the same borrowing card a reader card, a library pass, or the local-language equivalent. A policy search that works for staff using official terms returns an unrelated event pass for visitors. The librarian asks the engineering team to preserve regional variation while giving patrons a source they can verify.

This fictional case continues through the lectures.

For a documented comparison, read [Who gets left out of a transcript?](../../casebook/speech-recognition.md).

## Entry prerequisites

- Courses 01–02 or equivalent experience
- Vectors and dot products
- Basic text processing

## Course outline

### Language and corpus preparation

- [01 · Why Language Is Hard](01-why-language-is-hard.md){ .study-lecture data-lecture="01-why-language-is-hard.md" }
- [02 · Corpora and Text Pipelines](02-corpora-and-text-pipelines.md){ .study-lecture data-lecture="02-corpora-and-text-pipelines.md" }

**Checkpoint**

Write an ambiguous search query. Normalize two spelling variants without discarding their original source text.

### Tokens and representations

- [03 · Tokenization](03-tokenization.md){ .study-lecture data-lecture="03-tokenization.md" }
- [04 · From Sparse Features to Embeddings](04-from-sparse-features-to-embeddings.md){ .study-lecture data-lecture="04-from-sparse-features-to-embeddings.md" }

**Checkpoint**

Compare the visible tokens for two search queries. Identify a distinct word that should retrieve the same policy.

### Search and indexing

- [05 · Similarity and Vector Search](05-similarity-and-vector-search.md){ .study-lecture data-lecture="05-similarity-and-vector-search.md" }
- [06 · Embedding Systems in Production](06-embedding-systems-in-production.md){ .study-lecture data-lecture="06-embedding-systems-in-production.md" }

**Checkpoint**

Record the top document for a token-overlap query and a synonym-only query. Explain the difference.

## Notebook workshop

Compare a direct password query with an alternate wording that shares no indexed terms. Use the scores to motivate a dense retrieval baseline.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Build and evaluate a multilingual semantic search engine with lexical and vector baselines.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Manning, Raghavan & Schütze — Introduction to Information Retrieval
- Mikolov et al. — Efficient Estimation of Word Representations in Vector Space

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
