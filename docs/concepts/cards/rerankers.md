# Rerankers

**Purpose:** Reference card for **rerankers** used across AIEBOK books and knowledge areas.

## Core explanation

Rerankers rescore top-k candidates with cross-attention models more accurate than bi-encoders alone. They add latency proportional to candidates rescored.

## Example

Cross-encoder reranking top-50 BM25 hits improves precision@5 for policy QA.

## Evidence of understanding

Measure nDCG@5 and p95 latency with reranker on versus off at k=50.

## Trade-offs

No mechanism is universal. Compare rerankers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
