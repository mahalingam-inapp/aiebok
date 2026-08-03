# Training

**Purpose:** Reference card for **training** used across AIEBOK books and knowledge areas.

## Core explanation

Training fits model parameters to data by minimizing a loss over many examples. It defines what behavior the model is rewarded for and must be separated from inference in operations.

## Example

Fine-tuning a classifier on support tickets teaches phrasing patterns that inference-time prompts alone may not stabilize.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Log training loss, validation loss, and one task metric per epoch and stop when validation degrades.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare training against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bias And Variance](../../concepts/cards/bias-and-variance.md)
- [Distribution Shift](../../concepts/cards/distribution-shift.md)
- [Generalization](../../concepts/cards/generalization.md)
- [Inference](../../concepts/cards/inference.md)

## Related chapters

- [05 Learning And Generalization](../../books/01-foundations-of-intelligence/05-learning-and-generalization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
