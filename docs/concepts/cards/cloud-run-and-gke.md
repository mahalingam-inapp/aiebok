# Cloud Run And Gke

**Purpose:** Reference card for **cloud run and gke** used across AIEBOK books and knowledge areas.

## Core explanation

Cloud Run and GKE deploy serverless containers and Kubernetes GPU workloads on Google Cloud.

## Example

Cloud Run serves CPU embedding API; GKE Autopilot runs LLM inference with TPU/GPU node pools.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document when Cloud Run max duration forces move to GKE for long jobs.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cloud run and gke against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cloud Iam](../../concepts/cards/cloud-iam.md)
- [Portable Interfaces](../../concepts/cards/portable-interfaces.md)
- [Vertex Ai](../../concepts/cards/vertex-ai.md)
- [Vertex Ai Search](../../concepts/cards/vertex-ai-search.md)

## Related chapters

- [05 Google Cloud And Portable Patterns](../../books/12-cloud-and-enterprise-ai-architecture/05-google-cloud-and-portable-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
