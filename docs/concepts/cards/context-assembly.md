# Context Assembly

**Purpose:** Reference card for **context assembly** used across AIEBOK books and knowledge areas.

## Core explanation

Context assembly is the pipeline that gathers instructions, state, evidence, tools, and examples into the final prompt. Order and separation affect model behavior.

## Example

Placing evidence after instructions but before the user question reduces instruction drift in long contexts.

## Evidence of understanding

Trace one request's assembly stages and verify each section matches the spec template.

## Trade-offs

No mechanism is universal. Compare context assembly against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
