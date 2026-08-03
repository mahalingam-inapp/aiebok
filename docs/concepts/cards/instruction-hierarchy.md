# Instruction Hierarchy

**Purpose:** Reference card for **instruction hierarchy** used across AIEBOK books and knowledge areas.

## Core explanation

Instruction hierarchy ranks system, developer, and user messages so lower-priority text cannot override safety or policy. It is essential when untrusted content appears in context.

## Example

Retrieved web pages must not outrank the system prompt forbidding credential disclosure.

## Evidence of understanding

Inject conflicting instructions at each level and verify system policy wins.

## Trade-offs

No mechanism is universal. Compare instruction hierarchy against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
