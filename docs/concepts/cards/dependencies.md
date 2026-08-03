# Dependencies

**Purpose:** Reference card for **dependencies** used across AIEBOK books and knowledge areas.

## Core explanation

Dependencies constrain execution order—step B requires output or state from step A. Violating them causes flaky failures or data corruption.

## Example

Sending customer emails before database migration commits references wrong product IDs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Topological sort the plan and simulate; flag any out-of-order execution.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare dependencies against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Goal Decomposition](../../concepts/cards/goal-decomposition.md)
- [Plan Representation](../../concepts/cards/plan-representation.md)
- [Replanning](../../concepts/cards/replanning.md)
- [State](../../concepts/cards/state.md)

## Related chapters

- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
