# Foundation Model APIs

## Capability

Managed access to frontier and open models via HTTP with auth, quotas, and policy hooks.

## When to use

Use when you need fast time-to-value without operating GPU clusters.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Amazon Bedrock |
| Azure | Azure OpenAI / Azure AI Foundry model deployments |
| Google Cloud | Vertex AI Model Garden / Gemini API |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Vendor lock-in, region availability gaps, and opaque model version changes.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
