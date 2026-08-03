# Regression

**Purpose:** Reference card for **regression** used across AIEBOK books and knowledge areas.

## Core explanation

Regression predicts continuous targets—latency, revenue, temperature—by minimizing loss over numeric outputs. Choice of loss (MSE, Huber) reflects outlier sensitivity in operations.

## Example

Forecasting queue wait time uses regression; thresholds on predicted minutes trigger staffing alerts.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare MAE and RMSE on a holdout set and inspect worst 5% errors for systematic bias.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare regression against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Classification](../../concepts/cards/classification.md)
- [Loss Functions](../../concepts/cards/loss-functions.md)
- [Optimization](../../concepts/cards/optimization.md)
- [Regularization](../../concepts/cards/regularization.md)

## Related chapters

- [02 Supervised Learning](../../books/02-machine-learning-systems/02-supervised-learning.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
