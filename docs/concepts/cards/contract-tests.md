# Contract Tests

**Purpose:** Reference card for **contract tests** used across AIEBOK books and knowledge areas.

## Core explanation

Contract tests verify integrations between services—API schemas, tool responses—without full end-to-end runs. They catch breaking changes early.

## Example

Consumer test asserts search API returns fields reranker expects.

## Evidence of understanding

Run contract tests in CI on every API schema change.

## Trade-offs

No mechanism is universal. Compare contract tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
