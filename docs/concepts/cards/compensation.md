# Compensation

**Purpose:** Reference card for **compensation** used across AIEBOK books and knowledge areas.

## Core explanation

Compensation undo or offsets partial effects when later steps fail—Saga pattern for agents. Without it, retries duplicate charges or records.

## Example

Failed booking after charge triggers automatic refund compensation transaction.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Simulate mid-saga failure and verify compensation returns system to pre-transaction state.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare compensation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Episodic Memory](../../concepts/cards/episodic-memory.md)
- [Idempotency](../../concepts/cards/idempotency.md)
- [Recovery](../../concepts/cards/recovery.md)

## Related chapters

- [03 Agent Memory And Recovery](../../books/08-agent-systems/03-agent-memory-and-recovery.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
