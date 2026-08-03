# Cloud Iam

**Purpose:** Reference card for **cloud iam** used across AIEBOK books and knowledge areas.

## Core explanation

Google Cloud IAM binds roles to identities for least-privilege access to Vertex, Storage, and BigQuery in AI pipelines.

## Example

Service account invokes Vertex prediction only; humans cannot read raw training bucket.

## Evidence of understanding

IAM policy audit: no allUsers on AI artifact buckets.

## Trade-offs

No mechanism is universal. Compare cloud iam against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
