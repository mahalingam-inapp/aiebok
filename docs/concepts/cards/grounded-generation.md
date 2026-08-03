# Grounded Generation

**Purpose:** Reference card for **grounded generation** used across AIEBOK books and knowledge areas.

## Core explanation

Grounded generation conditions answers strictly on provided evidence, refusing when support is insufficient. Prompts and validators enforce cite-or-abstain behavior.

## Example

The model quotes section 4.2 for refund rules instead of inventing a 30-day window.

## Evidence of understanding

Score faithfulness and abstention rate on cases with and without supporting passages.

## Trade-offs

No mechanism is universal. Compare grounded generation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
