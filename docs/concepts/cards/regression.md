# Regression

**Purpose:** Reference card for **regression** used across AIEBOK books and knowledge areas.

## Core explanation

Regression predicts continuous targets—latency, revenue, temperature—by minimizing loss over numeric outputs. Choice of loss (MSE, Huber) reflects outlier sensitivity in operations.

## Example

Forecasting queue wait time uses regression; thresholds on predicted minutes trigger staffing alerts.

## Evidence of understanding

Compare MAE and RMSE on a holdout set and inspect worst 5% errors for systematic bias.

## Trade-offs

No mechanism is universal. Compare regression against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
