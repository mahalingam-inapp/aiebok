# Loss Functions

**Purpose:** Reference card for **loss functions** used across AIEBOK books and knowledge areas.

## Core explanation

Loss functions score how wrong predictions are and drive optimization—cross-entropy for classes, MSE for regression, custom losses for ranking. The loss encodes what the system is punished for.

## Example

Using focal loss down-weights easy negatives so a rare-defect detector trains on hard examples.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Train with two losses on the same data and compare which aligns with the business metric.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare loss functions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Classification](../../concepts/cards/classification.md)
- [Optimization](../../concepts/cards/optimization.md)
- [Regression](../../concepts/cards/regression.md)
- [Regularization](../../concepts/cards/regularization.md)

## Related chapters

- [02 Supervised Learning](../../books/02-machine-learning-systems/02-supervised-learning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
