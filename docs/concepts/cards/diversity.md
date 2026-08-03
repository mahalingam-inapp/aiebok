# Diversity

**Purpose:** Reference card for **diversity** used across AIEBOK books and knowledge areas.

## Core explanation

Diversity in context selection avoids redundant passages that waste tokens on repeated facts. Maximal marginal relevance is a common heuristic.

## Example

Three chunks saying the same PTO limit add no value; one plus related exceptions is better.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare unique fact coverage at fixed token budget with and without MMR selection.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare diversity against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Context Packing](../../concepts/cards/context-packing.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Reciprocal Rank Fusion](../../concepts/cards/reciprocal-rank-fusion.md)
- [Rerankers](../../concepts/cards/rerankers.md)

## Related chapters

- [04 Ranking And Context Selection](../../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
