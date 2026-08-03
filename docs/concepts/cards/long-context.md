# Long Context

**Purpose:** Reference card for **long context** used across AIEBOK books and knowledge areas.

## Core explanation

Long context models attend to hundred-thousand-plus tokens in one window—reducing need for retrieval but not eliminating cost or lost-in-middle effects.

## Example

Pasting entire contract for QA works until cost and middle-section attention degrade answers.

## Evidence of understanding

Compare long-context versus RAG on 50 questions requiring distant clause lookup.

## Trade-offs

No mechanism is universal. Compare long context against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
