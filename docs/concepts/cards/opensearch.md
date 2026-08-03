# Opensearch

**Purpose:** Reference card for **opensearch** used across AIEBOK books and knowledge areas.

## Core explanation

Amazon OpenSearch supports lexical, vector, and hybrid search with k-NN indexes for RAG on AWS.

## Example

OpenSearch k-NN index stores policy embeddings filtered by IAM-scoped document metadata.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Benchmark recall@10 and p95 query latency on OpenSearch versus managed alternative.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare opensearch against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Amazon Bedrock](../../concepts/cards/amazon-bedrock.md)
- [Cloudwatch And Iam](../../concepts/cards/cloudwatch-and-iam.md)
- [Lambda And Eks](../../concepts/cards/lambda-and-eks.md)
- [Sagemaker](../../concepts/cards/sagemaker.md)

## Related chapters

- [03 Aws Managed Ai](../../books/12-cloud-and-enterprise-ai-architecture/03-aws-managed-ai.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
