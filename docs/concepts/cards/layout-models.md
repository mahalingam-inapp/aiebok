# Layout Models

**Purpose:** Reference card for **layout models** used across AIEBOK books and knowledge areas.

## Core explanation

Layout models detect reading order, tables, figures, and headings in documents beyond raw OCR boxes.

## Example

Invoice layout model separates line items table from footer terms for field extraction.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Evaluate field F1 with layout-aware parsing versus OCR-only on 50 document layouts.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare layout models against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Document Ai](../../concepts/cards/document-ai.md)
- [Ocr](../../concepts/cards/ocr.md)
- [Vision Encoders](../../concepts/cards/vision-encoders.md)
- [Visual Grounding](../../concepts/cards/visual-grounding.md)

## Related chapters

- [01 Vision And Document Intelligence](../../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
