# Observability for LLM Systems

## Capability

Traces, metrics, and logs for prompts, retrieval, tools, and outputs.

## When to use

Use from day one—debugging RAG without traces is guesswork.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | CloudWatch, X-Ray, OpenTelemetry on Lambda/ECS |
| Azure | Azure Monitor, Application Insights |
| Google Cloud | Cloud Logging, Cloud Trace, custom metrics |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Logging raw prompts with PII into immutable log stores.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
