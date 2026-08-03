# Backtracking

**Purpose:** Reference card for **backtracking** used across AIEBOK books and knowledge areas.

## Core explanation

Backtracking abandons partial solutions that fail constraints and returns to earlier choices. Essential when early greedy decisions lock in errors.

## Example

If tool call returns 404, backtrack to alternate query formulation instead of hallucinating data.

## Evidence of understanding

Log backtrack events and measure recovery rate on injected tool failures.

## Trade-offs

No mechanism is universal. Compare backtracking against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
