# Secrets & Key Management

## Capability

Store API keys, DB credentials, and encryption keys safely.

## When to use

Use for every external model provider credential.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Secrets Manager, KMS |
| Azure | Key Vault |
| Google Cloud | Secret Manager, Cloud KMS |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Secrets in environment variables logged by crash dumps.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
