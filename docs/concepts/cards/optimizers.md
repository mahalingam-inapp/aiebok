# Optimizers

**Purpose:** Reference card for **optimizers** used across AIEBOK books and knowledge areas.

## Core explanation

Optimizers like Adam, AdamW, and SGD with momentum adapt update rules beyond vanilla gradient descent. They affect convergence speed, final loss, and generalization.

## Example

AdamW decouples weight decay from adaptive steps—common default for transformer fine-tuning.

## Evidence of understanding

Compare final validation metric and training time for Adam versus SGD on the same task.

## Trade-offs

No mechanism is universal. Compare optimizers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
