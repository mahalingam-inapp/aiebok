# Document Ingestion Pipelines

## Capability

Parse, chunk, enrich, and index documents with provenance.

## When to use

Use when source formats vary (PDF, HTML, tickets) and lineage matters.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Textract + Lambda + Step Functions, Bedrock KB ingestion |
| Azure | Document Intelligence + Azure Functions + AI Search indexers |
| Google Cloud | Document AI + Cloud Functions + Vertex Search importers |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

OCR errors and chunk-boundary mistakes propagate into RAG answers.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
