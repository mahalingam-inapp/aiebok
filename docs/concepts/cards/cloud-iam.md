# Cloud Iam

**Purpose:** Reference card for **cloud iam** used across AIEBOK books and knowledge areas.

## Core explanation

Google Cloud IAM binds roles to identities for least-privilege access to Vertex, Storage, and BigQuery in AI pipelines.

## Example

Service account invokes Vertex prediction only; humans cannot read raw training bucket.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

IAM policy audit: no allUsers on AI artifact buckets.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cloud iam against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cloud Run And Gke](../../concepts/cards/cloud-run-and-gke.md)
- [Portable Interfaces](../../concepts/cards/portable-interfaces.md)
- [Vertex Ai](../../concepts/cards/vertex-ai.md)
- [Vertex Ai Search](../../concepts/cards/vertex-ai-search.md)

## Related chapters

- [05 Google Cloud And Portable Patterns](../../books/12-cloud-and-enterprise-ai-architecture/05-google-cloud-and-portable-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
