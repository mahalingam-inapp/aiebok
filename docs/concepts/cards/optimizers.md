# Optimizers

**Purpose:** Reference card for **optimizers** used across AIEBOK books and knowledge areas.

## Core explanation

Optimizers like Adam, AdamW, and SGD with momentum adapt update rules beyond vanilla gradient descent. They affect convergence speed, final loss, and generalization.

## Example

AdamW decouples weight decay from adaptive steps—common default for transformer fine-tuning.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare final validation metric and training time for Adam versus SGD on the same task.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare optimizers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Activations](../../concepts/cards/activations.md)
- [Backpropagation](../../concepts/cards/backpropagation.md)
- [Neurons And Layers](../../concepts/cards/neurons-and-layers.md)
- [Normalization](../../concepts/cards/normalization.md)

## Related chapters

- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
