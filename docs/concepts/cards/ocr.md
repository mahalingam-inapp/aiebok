# Ocr

**Purpose:** Reference card for **ocr** used across AIEBOK books and knowledge areas.

## Core explanation

OCR extracts text from scanned images and photos, introducing recognition errors that propagate to chunks and answers. Confidence scores help gate low-quality extractions.

## Example

Scanned contracts with skewed pages need deskew preprocessing before OCR.

## Evidence of understanding

Report word-error rate on ten scanned pages and abstain when mean confidence < threshold.

## Trade-offs

No mechanism is universal. Compare ocr against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
