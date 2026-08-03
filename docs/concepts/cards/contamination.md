# Contamination

**Purpose:** Reference card for **contamination** used across AIEBOK books and knowledge areas.

## Core explanation

Contamination occurs when eval examples leak into training data, inflating benchmark scores.

## Example

Near-duplicate test questions in fine-tune set invalidate held-out claims.

## Evidence of understanding

Run n-gram or embedding overlap check between train and eval; zero high overlap pairs.

## Trade-offs

No mechanism is universal. Compare contamination against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
