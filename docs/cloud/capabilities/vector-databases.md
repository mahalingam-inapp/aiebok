# Vector Databases

## Capability

Approximate nearest-neighbor search at scale with metadata filtering.

## When to use

Use when dense retrieval must serve millions+ vectors with ACL filters.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | OpenSearch k-NN, Aurora pgvector, Bedrock Knowledge Bases |
| Azure | Azure AI Search vector fields, Cosmos DB vector |
| Google Cloud | Vertex AI Vector Search, AlloyDB pgvector |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Recall/latency trade-offs and reindex cost during embedding model upgrades.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
