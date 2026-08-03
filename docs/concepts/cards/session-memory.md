# Session Memory

**Purpose:** Reference card for **session memory** used across AIEBOK books and knowledge areas.

## Core explanation

Session memory persists within a conversation—recent turns, pending clarifications—without long-term storage. TTL and summarization policies prevent unbounded growth.

## Example

Remembering the user's chosen account ID this session avoids re-asking on every message.

## Evidence of understanding

Measure token growth over 20-turn dialogues with and without rolling summarization.

## Trade-offs

No mechanism is universal. Compare session memory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
