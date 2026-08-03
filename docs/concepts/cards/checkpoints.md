# Checkpoints

**Purpose:** Reference card for **checkpoints** used across AIEBOK books and knowledge areas.

## Core explanation

Checkpoints persist durable agent state so interrupted runs resume without repeating side effects.

## Example

After approval gate, checkpoint stores pending payment until human approves, then continues.

## When to use

Use when tasks require multi-step decisions, tool use, or recovery across variable inputs.

## When not to use

Skip when a deterministic workflow with fixed steps is clearer and safer.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Bound steps, cost, tools, and human approval for side effects.

## Evidence of understanding

Kill run mid-loop, restore checkpoint, verify idempotent tools are not duplicated.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare checkpoints against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Compensation](../../concepts/cards/compensation.md)
- [Data Mixtures](../../concepts/cards/data-mixtures.md)
- [Episodic Memory](../../concepts/cards/episodic-memory.md)
- [Idempotency](../../concepts/cards/idempotency.md)

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [03 Agent Memory And Recovery](../../books/08-agent-systems/03-agent-memory-and-recovery.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
