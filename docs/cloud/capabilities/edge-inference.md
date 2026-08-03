# Edge & On-Device Inference

## Capability

Run smaller models close to users or devices.

## When to use

Use for latency-sensitive or offline scenarios.

## Provider mapping

| Provider | Typical services |
|---|---|
| AWS | SageMaker Edge, IoT Greengrass patterns |
| Azure | Azure IoT Edge, ONNX on devices |
| Google Cloud | Edge TPU / mobile deployment via TFLite |

## Engineering checklist

1. Define the enduring capability independent of vendor names.
2. Map identity, network, and data boundaries before choosing SKUs.
3. Benchmark latency, cost, and quality on *your* workload—not generic benchmarks.
4. Document model/index versions and rollback steps in an ADR.
5. Add observability for retrieval, prompts, tools, and outputs.

## Common pitfalls

Model size limits and update distribution complexity.

## Related study

- [Cloud capability map](../index.md)
- [Enterprise AI building blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)
- [Identity and trust boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)
