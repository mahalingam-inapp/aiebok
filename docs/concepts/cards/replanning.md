# Replanning

**Purpose:** Reference card for **replanning** used across AIEBOK books and knowledge areas.

## Core explanation

Replanning updates the action sequence when observations invalidate assumptions. Static plans fail in open environments with changing data.

## Example

If inventory check shows zero stock, replan from 'ship item' to 'notify backorder'.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Inject mid-run observation changes and measure replan latency and success rate.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare replanning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Dependencies](../../concepts/cards/dependencies.md)
- [Goal Decomposition](../../concepts/cards/goal-decomposition.md)
- [Plan Representation](../../concepts/cards/plan-representation.md)
- [State](../../concepts/cards/state.md)

## Related chapters

- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
