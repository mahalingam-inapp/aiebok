# State

**Purpose:** Reference card for **state** used across AIEBOK books and knowledge areas.

## Core explanation

State captures variables the system believes true at a point in execution—inventory, user intent, pending approvals. Explicit state enables recovery and verification.

## Example

Agent state tracks current_step, artifacts_created, and budget_remaining across turns.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Serialize and deserialize state; resume mid-run and verify identical next action.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare state against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Budgets](../../concepts/cards/budgets.md)
- [Dependencies](../../concepts/cards/dependencies.md)
- [Goal Decomposition](../../concepts/cards/goal-decomposition.md)
- [Plan Act Observe](../../concepts/cards/plan-act-observe.md)

## Related chapters

- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
