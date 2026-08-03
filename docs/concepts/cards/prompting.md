# Prompting

**Purpose:** Reference card for **prompting** used across AIEBOK books and knowledge areas.

## Core explanation

Prompting steers model behavior at inference via instructions and examples without weight updates. It is the fastest iteration path when context fits.

## Example

Adding 'cite sources' instruction improves citation rate without retraining.

## Evidence of understanding

Compare prompt variants on behavioral eval with fixed model weights.

## Trade-offs

No mechanism is universal. Compare prompting against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
