# Session Memory

**Purpose:** Reference card for **session memory** used across AIEBOK books and knowledge areas.

## Core explanation

Session memory persists within a conversation—recent turns, pending clarifications—without long-term storage. TTL and summarization policies prevent unbounded growth.

## Example

Remembering the user's chosen account ID this session avoids re-asking on every message.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure token growth over 20-turn dialogues with and without rolling summarization.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare session memory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Long Term Memory](../../concepts/cards/long-term-memory.md)
- [Memory Retrieval](../../concepts/cards/memory-retrieval.md)
- [Summarization](../../concepts/cards/summarization.md)
- [Working Memory](../../concepts/cards/working-memory.md)

## Related chapters

- [04 Conversation And Memory](../../books/05-prompt-and-context-engineering/04-conversation-and-memory.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
