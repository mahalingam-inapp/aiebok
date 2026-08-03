# Search

**Purpose:** Reference card for **search** used across AIEBOK books and knowledge areas.

## Core explanation

Search explores a space of partial solutions—plans, code candidates, tool sequences—guided by heuristics and budgets. Inference-time search trades compute for accuracy.

## Example

Tree-of-thought explores multiple math solution paths before committing to an answer.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Plot accuracy versus number of nodes expanded with a fixed timeout.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare search against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Backtracking](../../concepts/cards/backtracking.md)
- [Decomposition](../../concepts/cards/decomposition.md)
- [Heuristics](../../concepts/cards/heuristics.md)
- [Termination](../../concepts/cards/termination.md)

## Related chapters

- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
