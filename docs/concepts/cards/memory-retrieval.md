# Memory Retrieval

**Purpose:** Reference card for **memory retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Memory retrieval selects relevant past facts given the current query—vector search, keyword, or structured lookup. Irrelevant memories pollute context and cause confabulation.

## Example

Retrieving only memories tagged with the current project ID avoids cross-project contamination.

## Evidence of understanding

Measure precision@5 of retrieved memories on labeled session continuations.

## Trade-offs

No mechanism is universal. Compare memory retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
