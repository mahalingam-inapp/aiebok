# Durable Execution

**Purpose:** Reference card for **durable execution** used across AIEBOK books and knowledge areas.

## Core explanation

Durable execution persists workflow state across process restarts and deploys—Temporal, Step Functions patterns. Long agents need this, not in-memory loops alone.

## Example

Day-long onboarding workflow survives server restart and resumes at last checkpoint.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Kill worker mid-run twice and verify exactly-once side effects for non-idempotent steps.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare durable execution against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cancellation](../../concepts/cards/cancellation.md)
- [Human Oversight](../../concepts/cards/human-oversight.md)
- [Leases](../../concepts/cards/leases.md)
- [Queues](../../concepts/cards/queues.md)

## Related chapters

- [06 Operating Long Running Agents](../../books/08-agent-systems/06-operating-long-running-agents.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
