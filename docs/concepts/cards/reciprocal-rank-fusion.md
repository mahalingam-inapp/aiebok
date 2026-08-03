# Reciprocal Rank Fusion

**Purpose:** Reference card for **reciprocal rank fusion** used across AIEBOK books and knowledge areas.

## Core explanation

Reciprocal rank fusion merges ranked lists by summing 1/(k + rank) per document across retrievers.

## Example

A document ranked third lexically and second densely outscores a single-list winner.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Fuse two hand-built rankings and verify the dual-high document gets top fused score.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare reciprocal rank fusion against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Context Packing](../../concepts/cards/context-packing.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Diversity](../../concepts/cards/diversity.md)
- [Rerankers](../../concepts/cards/rerankers.md)

## Related chapters

- [04 Ranking And Context Selection](../../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
