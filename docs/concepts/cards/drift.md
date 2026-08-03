# Drift

**Purpose:** Reference card for **drift** used across AIEBOK books and knowledge areas.

## Core explanation

Drift is change in input or label distributions over time—covariate, prior, or concept drift. Unmonitored drift erodes model value without code changes.

## Example

New product vocabulary after a launch shifts ticket text while labels stay stable—covariate drift.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Monitor population stability index or embedding centroid shift weekly with alert thresholds.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare drift against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Validation](../../concepts/cards/data-validation.md)
- [Experiment Tracking](../../concepts/cards/experiment-tracking.md)
- [Model Registry](../../concepts/cards/model-registry.md)
- [Monitoring](../../concepts/cards/monitoring.md)

## Related chapters

- [06 The Ml Lifecycle](../../books/02-machine-learning-systems/06-the-ml-lifecycle.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
