# Multimodal Document Pipeline

## Goal

OCR, layout, extraction with provenance.

## Overview

Build a pipeline that parses documents with OCR and layout analysis, extracts structured fields, and attaches provenance metadata for every value. Field-level eval measures extraction quality before downstream consumers trust the output.

## Architecture

Ingestion normalizes PDFs and images into page artifacts with layout blocks. OCR runs on scanned regions; digital text bypasses OCR where possible. Extraction models or rules map blocks to schema fields. Provenance records page, bbox, confidence, and pipeline version per field.

## Prerequisites

Complete the matching [guided book](../books/13-multimodal-and-frontier-systems/index.md) and related labs.

## Build phases

### 1. Parse/OCR

**Goal:** Convert documents into layout-aware text blocks.

**Steps:**
   - Detect digital text vs scanned regions per page.
   - Run OCR on scanned areas with local tesseract or mock OCR for CI.
   - Emit layout JSON: page, bbox, text, block_type.
   - Handle multi-column and table regions with basic structure tags.

**Acceptance:**
   - Digital PDFs preserve text without unnecessary OCR.
   - OCR output includes confidence scores per block.
   - Layout JSON validates against internal schema.

   **Commands:**

   ```bash
   python doc/parse.py --input samples/invoice.pdf --out tmp/layout.json
   python doc/ocr.py --image samples/scan.png --out tmp/ocr.json
   python -m pytest tests/test_parse_ocr.py -q
   ```
### 2. Field eval

**Goal:** Measure extraction accuracy per field on labeled documents.

**Steps:**
   - Label gold set with field values and acceptable normalization rules.
   - Run extraction pipeline; compare with fuzzy match for dates and amounts.
   - Report precision/recall per field and per document type.
   - Add regression cases for past extraction failures.

**Acceptance:**
   - Primary fields (total, date, vendor) meet F1 threshold on gold set.
   - Eval distinguishes OCR errors from extraction logic errors.
   - Field metrics exported JSON for CI gate.

   **Commands:**

   ```bash
   python eval/field_eval.py --gold data/doc_gold.jsonl --pred tmp/extracted.jsonl
   python eval/field_eval.py --report --out reports/field_eval.json
   ```
### 3. Provenance metadata

**Goal:** Attach traceable source pointers to every extracted field.

**Steps:**
   - Define provenance schema: field, value, page, bbox, source_block_id, pipeline_version.
   - Populate provenance during extraction from layout block references.
   - Expose provenance in API response for UI highlighting.
   - Verify provenance resolves to existing blocks on validation pass.

**Acceptance:**
   - Every non-null field includes provenance with valid block reference.
   - UI or CLI can highlight source region from provenance alone.
   - Pipeline version recorded for audit replay.

   **Commands:**

   ```bash
   python extract/run.py --layout tmp/layout.json --schema invoice/v1 --out tmp/extracted.json
   python provenance/verify.py --extracted tmp/extracted.json --layout tmp/layout.json
   ```

## Troubleshooting

- OCR garbage on tables: detect table regions and route to specialized parser.
- Field eval inflated by easy digital PDFs: stratify metrics by scan vs digital subsets.
- Provenance bbox drift: store normalized coordinates relative to page dimensions.
- Slow pipeline: cache layout JSON and parallelize per-page OCR.

## Related patterns

- [Structured Output Validation](../patterns/structured-output-validation.md)
- [Human Review Queue](../patterns/human-review-queue.md)
- [Parent Child Chunks](../patterns/parent-child-chunks.md)
- [Uncertainty Disclosure](../patterns/uncertainty-disclosure.md)

## Related labs

- [1301 Vision And Document Intelligence](../labs/1301-vision-and-document-intelligence.md)
- [0602 Document Ingestion](../labs/0602-document-ingestion.md)
- [0502 Structured Generation](../labs/0502-structured-generation.md)
- [1002 Metrics And Human Judgment](../labs/1002-metrics-and-human-judgment.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
