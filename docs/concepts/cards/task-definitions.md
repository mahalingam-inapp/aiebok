# Task Definitions

**Purpose:** Reference card for **task definitions** used across AIEBOK books and knowledge areas.

## Core explanation

Task definitions specify input, expected output, constraints, and graders for eval cases. Vague tasks produce noisy, incomparable metrics.

## Example

'Summarize ticket' becomes 'Extract product, issue, sentiment JSON matching schema X'.

## Evidence of understanding

Peer-review ten task definitions for ambiguity before adding to gold set.

## Trade-offs

No mechanism is universal. Compare task definitions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
