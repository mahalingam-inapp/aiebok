# Cross Validation

**Purpose:** Reference card for **cross validation** used across AIEBOK books and knowledge areas.

## Core explanation

Cross-validation rotates train and validation folds to estimate performance variance with limited data. It reduces luck from a single split but must respect temporal or group structure when required.

## Example

K-fold on i.i.d. tabular data estimates variance; time-series tasks need forward-chaining instead.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report mean and standard deviation of the metric across folds, not just the best fold.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cross validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Calibration](../../concepts/cards/calibration.md)
- [Confusion Matrix](../../concepts/cards/confusion-matrix.md)
- [Precision And Recall](../../concepts/cards/precision-and-recall.md)
- [Slice Analysis](../../concepts/cards/slice-analysis.md)

## Related chapters

- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
