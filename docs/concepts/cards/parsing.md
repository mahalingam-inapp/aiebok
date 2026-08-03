# Parsing

**Purpose:** Reference card for **parsing** used across AIEBOK books and knowledge areas.

## Core explanation

Parsing converts documents—PDF, HTML, DOCX—into clean text and structure for indexing. Bad parsing loses tables, headings, and lists that retrieval cannot recover.

## Example

OCR garbling a table of limits makes correct retrieval impossible regardless of embedding quality.

## Evidence of understanding

Measure character-error rate and table cell accuracy on 50 representative documents.

## Trade-offs

No mechanism is universal. Compare parsing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
