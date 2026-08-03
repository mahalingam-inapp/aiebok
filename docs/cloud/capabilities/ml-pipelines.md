# ML & LLM Pipelines

## Capability

Orchestrated train/eval/deploy workflows with reproducible steps.

## When to use

Use when eval-gated promotion requires repeatable automation.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | SageMaker Pipelines, Step Functions |
| Azure | Azure ML pipelines, MLflow |
| Google Cloud | Vertex Pipelines, Kubeflow on GKE |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Pipeline fragility if secrets, data paths, and versions are implicit.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
