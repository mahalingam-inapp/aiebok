# Long Term Memory

**Purpose:** Reference card for **long term memory** used across AIEBOK books and knowledge areas.

## Core explanation

Long-term memory stores durable facts—preferences, past resolutions—retrieved selectively for future sessions. It requires consent, expiry, and correction paths.

## Example

Storing preferred language and timezone reduces friction but must be deletable on request.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Test memory write, retrieval, update, and deletion with audit logs for GDPR requests.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare long term memory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Memory Retrieval](../../concepts/cards/memory-retrieval.md)
- [Session Memory](../../concepts/cards/session-memory.md)
- [Summarization](../../concepts/cards/summarization.md)
- [Working Memory](../../concepts/cards/working-memory.md)

## Related chapters

- [04 Conversation And Memory](../../books/05-prompt-and-context-engineering/04-conversation-and-memory.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
