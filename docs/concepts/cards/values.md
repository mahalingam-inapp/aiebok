# Values

**Purpose:** Reference card for **values** used across AIEBOK books and knowledge areas.

## Core explanation

Values carry the content aggregated by attention weights—what actually flows between positions. Weighted sums of values update each position's representation.

## Example

Attending to a verb's value brings predicate information into the subject's representation.

## Evidence of understanding

Compare hidden states with and without value projection on a toy attention module.

## Trade-offs

No mechanism is universal. Compare values against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
