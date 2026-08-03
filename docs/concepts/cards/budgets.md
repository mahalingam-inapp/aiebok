# Budgets

**Purpose:** Reference card for **budgets** used across AIEBOK books and knowledge areas.

## Core explanation

Budgets cap tokens, tool calls, wall time, or dollars per task or session. Hard budgets prevent runaway agents and make economics predictable.

## Example

A research agent stops after $0.50 API spend or ten tool calls, whichever comes first.

## Evidence of understanding

Verify 100% of runs respect budget caps in stress tests with tempting infinite loops.

## Trade-offs

No mechanism is universal. Compare budgets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
