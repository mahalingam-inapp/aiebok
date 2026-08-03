# Layout Models

**Purpose:** Reference card for **layout models** used across AIEBOK books and knowledge areas.

## Core explanation

Layout models detect reading order, tables, figures, and headings in documents beyond raw OCR boxes.

## Example

Invoice layout model separates line items table from footer terms for field extraction.

## Evidence of understanding

Evaluate field F1 with layout-aware parsing versus OCR-only on 50 document layouts.

## Trade-offs

No mechanism is universal. Compare layout models against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
