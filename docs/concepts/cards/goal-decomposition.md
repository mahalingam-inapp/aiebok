# Goal Decomposition

**Purpose:** Reference card for **goal decomposition** used across AIEBOK books and knowledge areas.

## Core explanation

Goal decomposition maps a top-level objective into subgoals with success conditions and dependencies. It clarifies what 'done' means at each level.

## Example

'Ship feature' decomposes into spec approved, code merged, eval passed, and canary clean.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Validate dependency graph: no circular deps and every leaf goal is testable.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare goal decomposition against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Dependencies](../../concepts/cards/dependencies.md)
- [Plan Representation](../../concepts/cards/plan-representation.md)
- [Replanning](../../concepts/cards/replanning.md)
- [State](../../concepts/cards/state.md)

## Related chapters

- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
