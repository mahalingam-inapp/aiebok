# Termination

**Purpose:** Reference card for **termination** used across AIEBOK books and knowledge areas.

## Core explanation

Termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Without them, systems loop indefinitely.

## Example

Stop after five tool calls, success, or three consecutive no-progress iterations.

## Evidence of understanding

Verify 100% of test runs halt within max_steps and document stop reason distribution.

## Trade-offs

No mechanism is universal. Compare termination against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
