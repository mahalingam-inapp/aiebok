# Plan Representation

**Purpose:** Reference card for **plan representation** used across AIEBOK books and knowledge areas.

## Core explanation

Plan representation encodes steps, preconditions, effects, and dependencies in structures machines can validate—DAGs, STRIPS, or typed JSON plans.

## Example

A migration plan lists DB schema change before app deploy as a hard dependency edge.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Reject plans where any step's preconditions are unmet given simulated initial state.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare plan representation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Dependencies](../../concepts/cards/dependencies.md)
- [Goal Decomposition](../../concepts/cards/goal-decomposition.md)
- [Replanning](../../concepts/cards/replanning.md)
- [State](../../concepts/cards/state.md)

## Related chapters

- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
