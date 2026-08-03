# State Spaces

**Purpose:** Reference card for **state spaces** used across AIEBOK books and knowledge areas.

## Core explanation

A state space enumerates all configurations a system can occupy plus the actions that move between them. Explicit state models make search, planning, and verification tractable.

## Example

Warehouse robots represent position and load status as state; illegal moves (overweight pickup) are edges you never traverse.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

List states, actions, and goal conditions for one task and confirm every action has a defined transition.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare state spaces against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A](../../concepts/cards/a.md)
- [Breadth First Search](../../concepts/cards/breadth-first-search.md)
- [Heuristics](../../concepts/cards/heuristics.md)
- [Planning](../../concepts/cards/planning.md)

## Related chapters

- [03 Search Planning And Decisions](../../books/01-foundations-of-intelligence/03-search-planning-and-decisions.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
