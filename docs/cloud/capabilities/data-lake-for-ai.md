# Data Lake for AI Training & Eval

## Capability

Durable storage for corpora, eval sets, and experiment artifacts.

## When to use

Use when datasets are large and shared across teams.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | S3 + Glue catalog |
| Azure | ADLS Gen2 + Unity catalog patterns |
| Google Cloud | GCS + BigQuery external tables |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Missing ACLs on buckets containing sensitive fine-tune data.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
