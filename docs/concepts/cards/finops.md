# Finops

**Purpose:** Reference card for **finops** used across AIEBOK books and knowledge areas.

## Core explanation

FinOps tracks and optimizes AI spend—tokens, GPU hours, API fees—against business value.

## Example

Dashboard shows cost per successful ticket deflection by model route.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Monthly review: top three cost drivers and optimization actions with owner.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare finops against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Canaries](../../concepts/cards/canaries.md)
- [Continuous Evaluation](../../concepts/cards/continuous-evaluation.md)
- [Service Catalog](../../concepts/cards/service-catalog.md)
- [Slos](../../concepts/cards/slos.md)

## Related chapters

- [06 Llmops](../../books/11-training-serving-and-ai-operations/06-llmops.md)
- [06 Enterprise Operating Model](../../books/12-cloud-and-enterprise-ai-architecture/06-enterprise-operating-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
