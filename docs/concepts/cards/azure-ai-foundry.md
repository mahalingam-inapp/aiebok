# Azure Ai Foundry

**Purpose:** Reference card for **azure ai foundry** used across AIEBOK books and knowledge areas.

## Core explanation

Azure AI Foundry is Microsoft's unified portal for model deployment, fine-tuning, evaluation, and agent tooling integrated with Azure services.

## Example

Deploy GPT-4o mini, run eval flow, and promote to managed endpoint from Foundry pipeline.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Trace model from Foundry project through to production endpoint with eval artifact link.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare azure ai foundry against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Aks And Functions](../../concepts/cards/aks-and-functions.md)
- [Azure Ai Search](../../concepts/cards/azure-ai-search.md)
- [Azure Openai](../../concepts/cards/azure-openai.md)
- [Entra Id And Monitor](../../concepts/cards/entra-id-and-monitor.md)

## Related chapters

- [04 Azure Managed Ai](../../books/12-cloud-and-enterprise-ai-architecture/04-azure-managed-ai.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
