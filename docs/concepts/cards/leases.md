# Leases

**Purpose:** Reference card for **leases** used across AIEBOK books and knowledge areas.

## Core explanation

Leases grant temporary exclusive ownership of a resource—document, ticket, shard—preventing duplicate processing. Expired leases must reclaim safely.

## Example

Worker holds 60s lease on ticket; another worker picks up only after lease expiry.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Simulate worker death before lease expiry and verify safe reassignment.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare leases against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cancellation](../../concepts/cards/cancellation.md)
- [Durable Execution](../../concepts/cards/durable-execution.md)
- [Human Oversight](../../concepts/cards/human-oversight.md)
- [Queues](../../concepts/cards/queues.md)

## Related chapters

- [06 Operating Long Running Agents](../../books/08-agent-systems/06-operating-long-running-agents.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
