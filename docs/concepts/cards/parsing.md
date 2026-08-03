# Parsing

**Purpose:** Reference card for **parsing** used across AIEBOK books and knowledge areas.

## Core explanation

Parsing converts documents—PDF, HTML, DOCX—into clean text and structure for indexing. Bad parsing loses tables, headings, and lists that retrieval cannot recover.

## Example

OCR garbling a table of limits makes correct retrieval impossible regardless of embedding quality.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure character-error rate and table cell accuracy on 50 representative documents.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare parsing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Chunking](../../concepts/cards/chunking.md)
- [Metadata](../../concepts/cards/metadata.md)
- [Ocr](../../concepts/cards/ocr.md)
- [Provenance](../../concepts/cards/provenance.md)

## Related chapters

- [02 Document Ingestion](../../books/06-knowledge-and-retrieval-systems/02-document-ingestion.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
