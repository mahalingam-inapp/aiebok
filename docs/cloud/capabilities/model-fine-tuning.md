# Model Fine-Tuning Services

## Capability

Managed post-training on private data with job tracking.

## When to use

Use when prompt/RAG cannot meet style or format requirements.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Bedrock model customization, SageMaker training jobs |
| Azure | Azure OpenAI fine-tuning, Azure ML fine-tune pipelines |
| Google Cloud | Vertex supervised fine-tuning / tuning jobs |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Overfitting small datasets and eval gaps before promotion.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
