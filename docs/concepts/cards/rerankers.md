# Rerankers

**Purpose:** Reference card for **rerankers** used across AIEBOK books and knowledge areas.

## Core explanation

Rerankers rescore top-k candidates with cross-attention models more accurate than bi-encoders alone. They add latency proportional to candidates rescored.

## Example

Cross-encoder reranking top-50 BM25 hits improves precision@5 for policy QA.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Measure nDCG@5 and p95 latency with reranker on versus off at k=50.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare rerankers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Context Packing](../../concepts/cards/context-packing.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Diversity](../../concepts/cards/diversity.md)
- [Reciprocal Rank Fusion](../../concepts/cards/reciprocal-rank-fusion.md)

## Related chapters

- [04 Ranking And Context Selection](../../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
