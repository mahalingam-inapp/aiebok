# Memory Retrieval

**Purpose:** Reference card for **memory retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Memory retrieval selects relevant past facts given the current query—vector search, keyword, or structured lookup. Irrelevant memories pollute context and cause confabulation.

## Example

Retrieving only memories tagged with the current project ID avoids cross-project contamination.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Measure precision@5 of retrieved memories on labeled session continuations.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare memory retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Long Term Memory](../../concepts/cards/long-term-memory.md)
- [Session Memory](../../concepts/cards/session-memory.md)
- [Summarization](../../concepts/cards/summarization.md)
- [Working Memory](../../concepts/cards/working-memory.md)

## Related chapters

- [04 Conversation And Memory](../../books/05-prompt-and-context-engineering/04-conversation-and-memory.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
