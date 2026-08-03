# Model Registry

**Purpose:** Reference card for **model registry** used across AIEBOK books and knowledge areas.

## Core explanation

A model registry stores versioned models with stage labels—staging, production, archived—and metadata for audit. It is the handoff point between ML and serving teams.

## Example

Promoting v3.2 to production requires passing eval gates linked in the registry entry.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Trace one production prediction back to registry version, training data hash, and eval report.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare model registry against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Validation](../../concepts/cards/data-validation.md)
- [Drift](../../concepts/cards/drift.md)
- [Experiment Tracking](../../concepts/cards/experiment-tracking.md)
- [Monitoring](../../concepts/cards/monitoring.md)

## Related chapters

- [06 The Ml Lifecycle](../../books/02-machine-learning-systems/06-the-ml-lifecycle.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
