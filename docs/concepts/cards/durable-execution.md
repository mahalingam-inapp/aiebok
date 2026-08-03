# Durable Execution

**Purpose:** Reference card for **durable execution** used across AIEBOK books and knowledge areas.

## Core explanation

Durable execution persists workflow state across process restarts and deploys—Temporal, Step Functions patterns. Long agents need this, not in-memory loops alone.

## Example

Day-long onboarding workflow survives server restart and resumes at last checkpoint.

## Evidence of understanding

Kill worker mid-run twice and verify exactly-once side effects for non-idempotent steps.

## Trade-offs

No mechanism is universal. Compare durable execution against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
