# Private Networking for AI

## Capability

VPC/VNet isolation, private endpoints, and egress control.

## When to use

Use when data residency and exfiltration risk matter.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | VPC endpoints for Bedrock/SageMaker, PrivateLink |
| Azure | Private endpoints for Azure OpenAI, VNet integration |
| Google Cloud | VPC-SC, Private Service Connect |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Misconfigured DNS breaking managed service resolution.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
