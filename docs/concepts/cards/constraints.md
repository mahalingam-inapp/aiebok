# Constraints

**Purpose:** Reference card for **constraints** used across AIEBOK books and knowledge areas.

## Core explanation

Constraints specify forbidden actions, length limits, formats, and scope boundaries in prompts. They reduce search space but must be testable.

## Example

'Do not mention competitors' and 'max 100 words' are enforceable constraints for eval.

## Evidence of understanding

Run constraint-violation checks on 100 outputs and track violation rate per release.

## Trade-offs

No mechanism is universal. Compare constraints against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
