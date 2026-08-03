# Backtracking

**Purpose:** Reference card for **backtracking** used across AIEBOK books and knowledge areas.

## Core explanation

Backtracking abandons partial solutions that fail constraints and returns to earlier choices. Essential when early greedy decisions lock in errors.

## Example

If tool call returns 404, backtrack to alternate query formulation instead of hallucinating data.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Log backtrack events and measure recovery rate on injected tool failures.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare backtracking against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Decomposition](../../concepts/cards/decomposition.md)
- [Heuristics](../../concepts/cards/heuristics.md)
- [Search](../../concepts/cards/search.md)
- [Termination](../../concepts/cards/termination.md)

## Related chapters

- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
