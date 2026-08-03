# Repair

**Purpose:** Reference card for **repair** used across AIEBOK books and knowledge areas.

## Core explanation

Repair loops attempt to fix invalid model outputs—re-prompting with errors, partial parsing, or constrained retries. They improve yield but add latency and cost.

## Example

When JSON is malformed, a repair prompt includes the parse error and asks for correction.

## Evidence of understanding

Track repair success rate and average extra tokens per successful repair.

## Trade-offs

No mechanism is universal. Compare repair against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
