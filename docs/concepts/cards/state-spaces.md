# State Spaces

**Purpose:** Reference card for **state spaces** used across AIEBOK books and knowledge areas.

## Core explanation

A state space enumerates all configurations a system can occupy plus the actions that move between them. Explicit state models make search, planning, and verification tractable.

## Example

Warehouse robots represent position and load status as state; illegal moves (overweight pickup) are edges you never traverse.

## Evidence of understanding

List states, actions, and goal conditions for one task and confirm every action has a defined transition.

## Trade-offs

No mechanism is universal. Compare state spaces against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
