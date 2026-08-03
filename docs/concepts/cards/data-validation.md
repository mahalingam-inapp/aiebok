# Data Validation

**Purpose:** Reference card for **data validation** used across AIEBOK books and knowledge areas.

## Core explanation

Data validation checks schema, ranges, distributions, and freshness of incoming data before training or inference. Silent schema drift breaks pipelines quietly.

## Example

A new optional field arriving as null for 40% of rows should block training until investigated.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run validation rules on daily ingest and alert when any column exceeds drift thresholds.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Drift](../../concepts/cards/drift.md)
- [Experiment Tracking](../../concepts/cards/experiment-tracking.md)
- [Model Registry](../../concepts/cards/model-registry.md)
- [Monitoring](../../concepts/cards/monitoring.md)

## Related chapters

- [06 The Ml Lifecycle](../../books/02-machine-learning-systems/06-the-ml-lifecycle.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
