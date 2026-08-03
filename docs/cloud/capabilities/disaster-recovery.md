# Disaster Recovery for AI Services

## Capability

Backups, multi-region failover, and RPO/RTO for indexes and models.

## When to use

Use when assistants are business-critical.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Cross-region S3 replication, multi-AZ endpoints |
| Azure | Geo-redundant storage, paired regions |
| Google Cloud | Multi-region GCS, dual-region buckets |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Vector indexes rebuilt slowly without reindex runbooks.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
