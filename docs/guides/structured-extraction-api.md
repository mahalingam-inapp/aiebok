# Structured Extraction API

## Goal

Schema-validated extraction behind a REST boundary.

## Overview

Expose schema-validated structured extraction behind a REST boundary with a repair loop for malformed model output. Adversarial tests prove the API rejects injection and schema drift before production traffic arrives.

## Architecture

The API accepts documents or text plus a JSON Schema id. An extractor prompt requests structured output; a validator enforces the schema; a repair loop re-prompts on failure with error context. Responses include validation status, parsed object, and repair attempt count. Adversarial tests run in CI.

## Prerequisites

Complete the matching [guided book](../books/05-prompt-and-context-engineering/index.md) and related labs.

## Build phases

### 1. JSON Schema

**Goal:** Define strict extraction targets with documented fields.

**Steps:**
   - Author schemas per extraction task with required fields and enums.
   - Register schemas in a catalog with version ids.
   - Add examples and counterexamples in schema descriptions for prompt grounding.
   - Validate schemas themselves with ajv or jsonschema CLI.

**Acceptance:**
   - Every production schema has version semver and changelog entry.
   - Schemas reject additionalProperties unless explicitly allowed.
   - Example instances validate successfully against their schema.

   **Commands:**

   ```bash
   python schemas/validate.py --schema schemas/invoice/v1.json
   python schemas/catalog.py --list
   ```
### 2. Validator

**Goal:** Parse and validate model output before returning to clients.

**Steps:**
   - Extract JSON from model response (strip markdown fences if present).
   - Run jsonschema validation; collect structured error paths.
   - Map validation failures to 422 responses with field-level detail.
   - Log raw model output only in secure debug mode.

**Acceptance:**
   - Valid outputs pass; missing required fields fail with explicit paths.
   - Validator handles unicode, nested objects, and array constraints.
   - No unvalidated JSON returned on success path.

   **Commands:**

   ```bash
   python extract/validate.py --schema invoice/v1 --input samples/raw_llm.txt
   python -m pytest tests/test_validator.py -q
   ```
### 3. Repair loop

**Goal:** Recover from minor formatting errors without user intervention.

**Steps:**
   - On validation failure, re-prompt with schema errors and prior output.
   - Cap repair attempts at 2; fail closed after exhaustion.
   - Track repair count in response metadata for quality monitoring.
   - Short-circuit if errors are non-recoverable (wrong types on root fields).

**Acceptance:**
   - Recoverable cases (truncated JSON, extra prose) succeed within 2 repairs.
   - Repair loop never infinite-loops; attempts bounded and logged.
   - Success rate on noisy sample set improves vs single-pass baseline.

   **Commands:**

   ```bash
   python extract/run.py --text samples/invoice.txt --schema invoice/v1 --repair
   python eval/repair_ablation.py --cases data/extraction_failures.jsonl
   ```
### 4. Adversarial tests

**Goal:** Verify resistance to injection and schema escape attempts.

**Steps:**
   - Build cases: instruction injection in source text, schema override attempts.
   - Assert API returns validation failure or sanitized output, never silent drift.
   - Test oversized inputs and nested depth limits.
   - Run adversarial suite in CI on every PR.

**Acceptance:**
   - Injection cases do not produce fields outside schema.
   - Oversized input rejected with 413 or truncated per policy.
   - CI fails on any adversarial case regression.

   **Commands:**

   ```bash
   python -m pytest tests/test_extraction_adversarial.py -q
   python eval/adversarial_extract.py --suite data/adversarial_extract.jsonl
   ```

## Troubleshooting

- Repair loop oscillates: include diff of prior errors and forbid repeating same malformed keys.
- Schema too strict for real documents: relax optional fields and use post-validation normalization.
- JSON buried in markdown: strengthen extraction regex and add a json-repair pre-pass.
- Latency spikes on repairs: cache schema compilation and parallelize only first pass in sync API.

## Related patterns

- [Structured Output Validation](../patterns/structured-output-validation.md)
- [Evaluator Optimizer](../patterns/evaluator-optimizer.md)
- [Adversarial Eval Suite](../patterns/adversarial-eval-suite.md)
- [Prompt Injection Guard](../patterns/prompt-injection-guard.md)

## Related labs

- [0502 Structured Generation](../labs/0502-structured-generation.md)
- [0501 Instructions That Work](../labs/0501-instructions-that-work.md)
- [1004 Security Of Ai Systems](../labs/1004-security-of-ai-systems.md)
- [1301 Vision And Document Intelligence](../labs/1301-vision-and-document-intelligence.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
