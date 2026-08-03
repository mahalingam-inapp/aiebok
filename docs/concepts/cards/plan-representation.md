# Plan Representation

**Purpose:** Reference card for **plan representation** used across AIEBOK books and knowledge areas.

## Core explanation

Plan representation encodes steps, preconditions, effects, and dependencies in structures machines can validate—DAGs, STRIPS, or typed JSON plans.

## Example

A migration plan lists DB schema change before app deploy as a hard dependency edge.

## Evidence of understanding

Reject plans where any step's preconditions are unmet given simulated initial state.

## Trade-offs

No mechanism is universal. Compare plan representation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
