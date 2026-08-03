# Gradient Descent

**Purpose:** Reference card for **gradient descent** used across AIEBOK books and knowledge areas.

## Core explanation

Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples. It is the workhorse optimizer behind most neural network training.

## Example

One SGD step on linear regression moves weights toward the line minimizing squared error on the mini-batch.

## Evidence of understanding

Hand-compute one update for noisy y = 2x + 1 data and confirm loss decreases on that batch.

## Trade-offs

No mechanism is universal. Compare gradient descent against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
