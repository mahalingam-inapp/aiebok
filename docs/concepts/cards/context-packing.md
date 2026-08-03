# Context Packing

**Purpose:** Reference card for **context packing** used across AIEBOK books and knowledge areas.

## Core explanation

Context packing fits selected passages into the token window respecting priority, citation needs, and truncation rules. Packing order affects what the model emphasizes.

## Example

Place highest-scored evidence first when middle-context attention is weaker in long windows.

## Evidence of understanding

Compare faithfulness when critical passage is first versus last at equal total tokens.

## Trade-offs

No mechanism is universal. Compare context packing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
