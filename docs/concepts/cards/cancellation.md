# Cancellation

**Purpose:** Reference card for **cancellation** used across AIEBOK books and knowledge areas.

## Core explanation

Cancellation stops in-flight agent work cleanly—revoke leases, abort tool calls, compensate partial effects. Users need cancel when plans change.

## Example

User cancels long research job; system stops tools and marks run cancelled, not failed.

## Evidence of understanding

Cancel at random steps and verify no orphaned side effects remain.

## Trade-offs

No mechanism is universal. Compare cancellation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
