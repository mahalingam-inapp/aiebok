# Context Traces

**Purpose:** Reference card for **context traces** used across AIEBOK books and knowledge areas.

## Core explanation

Context traces log the assembled prompt sections, token counts, and sources for debugging and compliance. They make probabilistic failures reproducible.

## Example

Replaying a failed answer with its trace shows whether retrieval or ranking dropped the key passage.

## Evidence of understanding

Sample 1% of requests with full traces retained for 30 days minimum.

## Trade-offs

No mechanism is universal. Compare context traces against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
