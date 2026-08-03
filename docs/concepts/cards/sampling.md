# Sampling

**Purpose:** Reference card for **sampling** used across AIEBOK books and knowledge areas.

## Core explanation

Sampling draws next tokens from the predicted distribution rather than always taking the argmax. It enables diverse outputs but introduces nondeterminism unless seeded.

## Example

Creative writing uses sampling; factual extraction often uses greedy or low-temperature decoding.

## Evidence of understanding

Generate 20 completions at temperature 0 versus 1 and measure factual consistency.

## Trade-offs

No mechanism is universal. Compare sampling against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
