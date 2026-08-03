# Compliance & Audit for AI

## Capability

Immutable logs, data retention, and evidence for regulators.

## When to use

Use in regulated industries deploying copilots.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | CloudTrail, Config, audit manager |
| Azure | Activity logs, Purview |
| Google Cloud | Audit logs, Assured Workloads |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Audit logs that omit retrieval document IDs.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
