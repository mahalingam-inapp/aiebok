# Delimiters

**Purpose:** Reference card for **delimiters** used across AIEBOK books and knowledge areas.

## Core explanation

Delimiters—XML tags, markdown fences, triple quotes—separate instructions from data so models parse structure reliably. Consistent delimiters reduce instruction–content bleed.

## Example

Wrapping user HTML in <document> tags prevents tags from being interpreted as instructions.

## Evidence of understanding

Test ten adversarial documents with and without delimiters and count instruction-following errors.

## Trade-offs

No mechanism is universal. Compare delimiters against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
