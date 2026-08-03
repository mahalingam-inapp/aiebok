# Gradient Descent

**Purpose:** Reference card for **gradient descent** used across AIEBOK books and knowledge areas.

## Core explanation

Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples. It is the workhorse optimizer behind most neural network training.

## Example

One SGD step on linear regression moves weights toward the line minimizing squared error on the mini-batch.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Hand-compute one update for noisy y = 2x + 1 data and confirm loss decreases on that batch.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare gradient descent against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Entropy](../../concepts/cards/entropy.md)
- [Matrix Transformations](../../concepts/cards/matrix-transformations.md)
- [Probability](../../concepts/cards/probability.md)
- [Vectors](../../concepts/cards/vectors.md)

## Related chapters

- [04 The Mathematics Engineers Need](../../books/01-foundations-of-intelligence/04-the-mathematics-engineers-need.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
