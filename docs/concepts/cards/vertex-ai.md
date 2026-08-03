# Vertex Ai

**Purpose:** Reference card for **vertex ai** used across AIEBOK books and knowledge areas.

## Core explanation

Google Vertex AI offers unified model training, tuning, deployment, and evaluation on GCP with Gemini and open models.

## Example

Fine-tune Gemini on proprietary data and deploy to private endpoint with VPC-SC.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare Vertex eval pipeline scores pre/post deploy on held-out set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare vertex ai against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cloud Iam](../../concepts/cards/cloud-iam.md)
- [Cloud Run And Gke](../../concepts/cards/cloud-run-and-gke.md)
- [Portable Interfaces](../../concepts/cards/portable-interfaces.md)
- [Vertex Ai Search](../../concepts/cards/vertex-ai-search.md)

## Related chapters

- [05 Google Cloud And Portable Patterns](../../books/12-cloud-and-enterprise-ai-architecture/05-google-cloud-and-portable-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
