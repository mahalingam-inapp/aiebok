# Container Model Serving

## Capability

Packaged inference servers (vLLM, TGI, Triton) on Kubernetes or managed containers.

## When to use

Use when you need open-weight models, custom routing, or on-prem parity.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | EKS + vLLM, ECS |
| Azure | AKS + custom containers |
| Google Cloud | GKE + Cloud Run GPU |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

You own patching, autoscaling, and GPU bin-packing efficiency.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
