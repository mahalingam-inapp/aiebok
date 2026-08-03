# Embedding APIs

## Capability

Batch or online text embedding for retrieval, clustering, and classification.

## When to use

Use when retrieval quality depends on a maintained embedding model lifecycle.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Bedrock Titan Embeddings, SageMaker endpoints |
| Azure | Azure OpenAI embeddings, Azure AI Foundry |
| Google Cloud | Vertex text embedding models |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Dimension/version mismatches between index and query break retrieval silently.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
