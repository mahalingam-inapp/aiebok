# Hybrid Search Services

## Capability

Lexical + semantic ranking in one managed search product.

## When to use

Use for enterprise document search with identifiers and paraphrases.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | OpenSearch hybrid queries, Kendra |
| Azure | Azure AI Search semantic ranker + BM25 |
| Google Cloud | Vertex AI Search |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Semantic ranker latency and tuning complexity vs. self-managed RRF.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
