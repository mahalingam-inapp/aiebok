# Amazon Bedrock

**Purpose:** Reference card for **amazon bedrock** used across AIEBOK books and knowledge areas.

## Core explanation

Amazon Bedrock provides managed access to foundation models from multiple providers via unified AWS APIs with IAM integration and private networking.

## Example

Invoke Claude and Titan through Bedrock in VPC without exposing keys on laptops.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare Bedrock latency and cost versus self-hosted on same region for target workload.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare amazon bedrock against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cloudwatch And Iam](../../concepts/cards/cloudwatch-and-iam.md)
- [Lambda And Eks](../../concepts/cards/lambda-and-eks.md)
- [Opensearch](../../concepts/cards/opensearch.md)
- [Sagemaker](../../concepts/cards/sagemaker.md)

## Related chapters

- [03 Aws Managed Ai](../../books/12-cloud-and-enterprise-ai-architecture/03-aws-managed-ai.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
