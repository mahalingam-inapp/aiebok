# Content Safety Filters

## Capability

Policy enforcement on inputs and outputs.

## When to use

Use for customer-facing assistants with abuse risk.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Bedrock Guardrails, Comprehend moderation |
| Azure | Azure AI Content Safety |
| Google Cloud | Vertex safety filters / Model Armor patterns |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

False positives blocking legitimate enterprise content.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
