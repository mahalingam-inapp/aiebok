# Cancellation

**Purpose:** Reference card for **cancellation** used across AIEBOK books and knowledge areas.

## Core explanation

Cancellation stops in-flight agent work cleanly—revoke leases, abort tool calls, compensate partial effects. Users need cancel when plans change.

## Example

User cancels long research job; system stops tools and marks run cancelled, not failed.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Cancel at random steps and verify no orphaned side effects remain.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cancellation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Durable Execution](../../concepts/cards/durable-execution.md)
- [Human Oversight](../../concepts/cards/human-oversight.md)
- [Leases](../../concepts/cards/leases.md)
- [Queues](../../concepts/cards/queues.md)

## Related chapters

- [06 Operating Long Running Agents](../../books/08-agent-systems/06-operating-long-running-agents.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
