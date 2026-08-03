# Vendor Management

**Purpose:** Reference card for **vendor management** used across AIEBOK books and knowledge areas.

## Core explanation

Vendor management evaluates AI providers on security, compliance, cost, performance, and exit strategy.

## Example

Annual review of OpenAI/Azure/Bedrock DPAs, data retention, and failover plan.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Maintain vendor scorecard with exit migration test date documented.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare vendor management against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Finops](../../concepts/cards/finops.md)
- [Service Catalog](../../concepts/cards/service-catalog.md)
- [Slos](../../concepts/cards/slos.md)
- [Team Topology](../../concepts/cards/team-topology.md)

## Related chapters

- [06 Enterprise Operating Model](../../books/12-cloud-and-enterprise-ai-architecture/06-enterprise-operating-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
