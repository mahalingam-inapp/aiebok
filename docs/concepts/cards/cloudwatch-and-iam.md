# Cloudwatch And Iam

**Purpose:** Reference card for **cloudwatch and iam** used across AIEBOK books and knowledge areas.

## Core explanation

CloudWatch and IAM deliver AWS monitoring, alerting, and access control for AI workloads—metrics, logs, roles, policies.

## Example

IAM role grants Bedrock invoke only; CloudWatch alarm on 5xx rate triggers runbook.

## Evidence of understanding

Least-privilege IAM review quarterly; zero overly broad bedrock:* on human roles.

## Trade-offs

No mechanism is universal. Compare cloudwatch and iam against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
