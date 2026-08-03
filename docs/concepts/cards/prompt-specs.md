# Prompt Specs

**Purpose:** Reference card for **prompt specs** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt specs version instructions, constraints, examples, and expected behaviors like API contracts. They enable review and regression unlike ad hoc prompts.

## Example

Prompt spec defines abstention when confidence low and JSON schema for outputs.

## Evidence of understanding

Diff prompt spec versions in CI and run regression eval on every change.

## Trade-offs

No mechanism is universal. Compare prompt specs against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
