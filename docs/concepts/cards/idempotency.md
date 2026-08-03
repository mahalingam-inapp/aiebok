# Idempotency

**Purpose:** Reference card for **idempotency** used across AIEBOK books and knowledge areas.

## Core explanation

Idempotent tools produce the same effect when called repeatedly with the same idempotency key. Agents retry safely only when tools support this.

## Example

create_ticket with idempotency key 'abc' must not spawn duplicate tickets on retry.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Call the same tool twice with identical keys and verify single side effect.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare idempotency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Compensation](../../concepts/cards/compensation.md)
- [Episodic Memory](../../concepts/cards/episodic-memory.md)
- [Function Calling](../../concepts/cards/function-calling.md)

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)
- [03 Agent Memory And Recovery](../../books/08-agent-systems/03-agent-memory-and-recovery.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
