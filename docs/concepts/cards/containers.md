# Containers

**Purpose:** Reference card for **containers** used across AIEBOK books and knowledge areas.

## Core explanation

Containers package model servers with dependencies for reproducible deployment across environments.

## Example

Docker image pins CUDA, Python, and model weights hash for prod inference.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Scan container image for CVEs; block deploy on critical unfixed vulnerabilities.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare containers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Autoscaling](../../concepts/cards/autoscaling.md)
- [Fallbacks](../../concepts/cards/fallbacks.md)
- [Model Routing](../../concepts/cards/model-routing.md)
- [Resilience](../../concepts/cards/resilience.md)

## Related chapters

- [05 Deployment And Routing](../../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
