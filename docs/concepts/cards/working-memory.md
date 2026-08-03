# Working Memory

**Purpose:** Reference card for **working memory** used across AIEBOK books and knowledge areas.

## Core explanation

Working memory holds transient state for the current turn—scratchpad notes, intermediate calculations—not durable across sessions. It clears when the task completes.

## Example

A calculator agent keeps running totals in working memory while parsing a multi-step word problem.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify working memory resets between unrelated tasks in the same session.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare working memory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Long Term Memory](../../concepts/cards/long-term-memory.md)
- [Memory Retrieval](../../concepts/cards/memory-retrieval.md)
- [Session Memory](../../concepts/cards/session-memory.md)
- [Summarization](../../concepts/cards/summarization.md)

## Related chapters

- [04 Conversation And Memory](../../books/05-prompt-and-context-engineering/04-conversation-and-memory.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
