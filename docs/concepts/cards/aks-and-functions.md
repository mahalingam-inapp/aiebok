# Aks And Functions

**Purpose:** Reference card for **aks and functions** used across AIEBOK books and knowledge areas.

## Core explanation

AKS and Azure Functions run containerized model servers and event-driven AI glue code on Azure.

## Example

Function triggers on blob upload; AKS serves GPU embedding model with HPA.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare cold start and cost for Functions versus always-on AKS for ingest path.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare aks and functions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Azure Ai Foundry](../../concepts/cards/azure-ai-foundry.md)
- [Azure Ai Search](../../concepts/cards/azure-ai-search.md)
- [Azure Openai](../../concepts/cards/azure-openai.md)
- [Entra Id And Monitor](../../concepts/cards/entra-id-and-monitor.md)

## Related chapters

- [04 Azure Managed Ai](../../books/12-cloud-and-enterprise-ai-architecture/04-azure-managed-ai.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
