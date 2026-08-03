# Workflow Orchestration

## Capability

Long-running AI workflows with retries and human steps.

## When to use

Use for multi-step ingestion, eval, and approval flows.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | Step Functions, MWAA |
| Azure | Logic Apps, Durable Functions |
| Google Cloud | Cloud Workflows, Composer |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

State machine sprawl without idempotent task design.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
