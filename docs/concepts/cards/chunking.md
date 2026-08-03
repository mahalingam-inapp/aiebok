# Chunking

**Purpose:** Reference card for **chunking** used across AIEBOK books and knowledge areas.

## Core explanation

Chunking splits documents into index units sized for retrieval precision and generation context. Boundaries should respect sections, not arbitrary token counts alone.

## Example

Splitting mid-table separates headers from values, producing useless retrieval hits.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Compare recall@5 with fixed-size versus section-aware chunking on table-heavy docs.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare chunking against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Metadata](../../concepts/cards/metadata.md)
- [Ocr](../../concepts/cards/ocr.md)
- [Parsing](../../concepts/cards/parsing.md)
- [Provenance](../../concepts/cards/provenance.md)

## Related chapters

- [02 Document Ingestion](../../books/06-knowledge-and-retrieval-systems/02-document-ingestion.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
