# Reciprocal Rank Fusion

**Purpose:** Reference card for **reciprocal rank fusion** used across AIEBOK books and knowledge areas.

## Core explanation

Reciprocal rank fusion merges ranked lists by summing 1/(k + rank) per document across retrievers.

## Example

A document ranked third lexically and second densely outscores a single-list winner.

## Evidence of understanding

Fuse two hand-built rankings and verify the dual-high document gets top fused score.

## Trade-offs

No mechanism is universal. Compare reciprocal rank fusion against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
