# Loss Functions

**Purpose:** Reference card for **loss functions** used across AIEBOK books and knowledge areas.

## Core explanation

Loss functions score how wrong predictions are and drive optimization—cross-entropy for classes, MSE for regression, custom losses for ranking. The loss encodes what the system is punished for.

## Example

Using focal loss down-weights easy negatives so a rare-defect detector trains on hard examples.

## Evidence of understanding

Train with two losses on the same data and compare which aligns with the business metric.

## Trade-offs

No mechanism is universal. Compare loss functions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
