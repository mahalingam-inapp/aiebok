# API Gateways for AI Services

## Capability

Rate limits, auth, routing, and request logging at the edge.

## When to use

Use when many clients hit shared model/retrieval backends.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | API Gateway, ALB |
| Azure | API Management, Application Gateway |
| Google Cloud | Apigee, Cloud Endpoints |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Gateway becomes a bottleneck without caching and routing rules.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
