# Lambda And Eks

**Purpose:** Reference card for **lambda and eks** used across AIEBOK books and knowledge areas.

## Core explanation

AWS Lambda and EKS provide serverless functions and Kubernetes clusters for AI orchestration, agents, and custom servers.

## Example

Lambda handles lightweight ingest triggers; EKS hosts vLLM GPU workloads with Karpenter scaling.

## Evidence of understanding

Map workload to Lambda versus EKS based on duration, GPU need, and cold-start tolerance.

## Trade-offs

No mechanism is universal. Compare lambda and eks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
