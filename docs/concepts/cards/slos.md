# Slos

**Purpose:** Reference card for **slos** used across AIEBOK books and knowledge areas.

## Core explanation

SLOs define target reliability and latency—availability, p95 latency, eval faithfulness—for AI platform services.

## Example

Gateway SLO: 99.9% availability, p95 <2s excluding model provider outages.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Error budget policy triggers feature freeze when SLO burn exceeds threshold.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare slos against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Finops](../../concepts/cards/finops.md)
- [Service Catalog](../../concepts/cards/service-catalog.md)
- [Team Topology](../../concepts/cards/team-topology.md)
- [Vendor Management](../../concepts/cards/vendor-management.md)

## Related chapters

- [06 Enterprise Operating Model](../../books/12-cloud-and-enterprise-ai-architecture/06-enterprise-operating-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
