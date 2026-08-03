# Identity for AI Workloads

## Capability

Authentication and authorization for humans, services, and agents.

## When to use

Use before any production model or retrieval endpoint.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | IAM roles, Identity Center, resource policies |
| Azure | Microsoft Entra ID, managed identities |
| Google Cloud | Cloud IAM, workload identity |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Over-broad API keys shared across environments.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
