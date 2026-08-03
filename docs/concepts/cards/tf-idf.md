# Tf Idf

**Purpose:** Reference card for **tf idf** used across AIEBOK books and knowledge areas.

## Core explanation

TF–IDF weights terms by local frequency and inverse document frequency, highlighting discriminative words in sparse retrieval. It is a strong lexical baseline before dense methods.

## Example

Searching 'PTO accrual cap' ranks handbook sections containing rare terms 'accrual' and 'cap' highly.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure recall@10 on 30 keyword-heavy queries against a dense baseline.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare tf idf against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [One Hot Vectors](../../concepts/cards/one-hot-vectors.md)
- [Sentence Embeddings](../../concepts/cards/sentence-embeddings.md)
- [Word Embeddings](../../concepts/cards/word-embeddings.md)

## Related chapters

- [04 From Sparse Features To Embeddings](../../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
