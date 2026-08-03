# Model Selection Harness

## Goal

Vendor-neutral benchmark report for task-specific model choice.

## Overview

Build a vendor-neutral benchmark harness that scores candidate models on your real tasks, logging quality, latency, and cost. The output is a selection ADR grounded in measured trade-offs, not vendor marketing.

## Architecture

The harness loads a fixed task dataset and routes each case to candidate model adapters behind a common interface. A run logger captures tokens, latency, and scores. Adapters wrap local mocks, open-weight endpoints, or API stubs so CI does not require live keys. Results feed a comparison report and ADR template.

## Prerequisites

Complete the matching [guided book](../books/04-transformers-and-foundation-models/index.md) and related labs.

## Build phases

### 1. Task dataset

**Goal:** Define representative tasks with gold references and scoring rubrics.

**Steps:**
   - Collect 30–100 cases spanning normal, boundary, and failure-prone inputs.
   - Attach expected outputs or rubric criteria per case.
   - Tag cases by slice: latency-sensitive, reasoning-heavy, structured output.
   - Freeze dataset version with checksum for reproducible runs.

**Acceptance:**
   - Dataset manifest includes version, checksum, and slice tag definitions.
   - Each case has an automated scorer or LLM-judge prompt with calibration set.
   - No duplicate or near-duplicate cases without explicit justification.

   **Commands:**

   ```bash
   python harness/validate_dataset.py --path data/model_tasks.jsonl
   python -c "import json; print(len(list(open('data/model_tasks.jsonl'))))"
   ```
### 2. Candidate models

**Goal:** Register models through a uniform adapter interface.

**Steps:**
   - Define adapter contract: complete(prompt, params) -> text, usage, latency_ms.
   - Implement adapters for local mock, small open-weight, and one API stub.
   - Configure per-model defaults: max_tokens, temperature, timeout.
   - Support batch mode for offline eval and single-case debug mode.

**Acceptance:**
   - All candidates pass a smoke test on three fixed prompts.
   - Adapter errors classified: timeout, rate_limit, invalid_output.
   - Mock adapter returns deterministic outputs for CI.

   **Commands:**

   ```bash
   python harness/adapters/mock.py --smoke
   python harness/run.py --model mock-small --cases data/model_tasks.jsonl --limit 5
   ```
### 3. Cost/latency log

**Goal:** Record operational metrics alongside quality scores.

**Steps:**
   - Log per-case: input_tokens, output_tokens, latency_ms, estimated_cost_usd.
   - Aggregate p50/p95 latency and cost per model and slice.
   - Flag cases where quality gains do not justify latency or cost increase.
   - Export run logs as JSONL for downstream dashboards.

**Acceptance:**
   - Every completed case has non-null latency and token counts.
   - Summary report includes quality, p95 latency, and cost per 1k cases.
   - Run reproducible with pinned dataset and adapter versions.

   **Commands:**

   ```bash
   python harness/run.py --models mock-small,mock-large --out logs/run.jsonl
   python harness/summarize.py --log logs/run.jsonl --out reports/compare.md
   ```
### 4. Selection ADR

**Goal:** Document the chosen model with evidence and rejected alternatives.

**Steps:**
   - Generate comparison table from run summaries.
   - Write ADR: context, decision, consequences, rejected options with metrics.
   - Define fallback model and routing rules for slice-specific overrides.
   - Link ADR to dataset version and harness commit hash.

**Acceptance:**
   - ADR cites numeric evidence for the primary model choice.
   - At least one alternative rejected with measured reason.
   - Fallback and override rules documented for ops handoff.

   **Commands:**

   ```bash
   python harness/adr_from_report.py --report reports/compare.md --out docs/adr/model-choice.md
   ```

## Troubleshooting

- Scores incomparable across models: normalize prompts and decoding params; use same tokenizer for length limits.
- Mock results mislead selection: reserve a held-out live eval for final sign-off even if CI uses mocks.
- High variance on small sets: increase case count or run multiple seeds and report confidence intervals.
- Latency dominated by cold start: warm up adapters before timed runs and report separately.

## Related patterns

- [Model Routing](../patterns/model-routing.md)
- [Fallback Cascade](../patterns/fallback-cascade.md)
- [Llm Judge Calibration](../patterns/llm-judge-calibration.md)
- [Adapter Swapping](../patterns/adapter-swapping.md)

## Related labs

- [0405 Inference And Sampling](../labs/0405-inference-and-sampling.md)
- [0406 Model Families And Selection](../labs/0406-model-families-and-selection.md)
- [1101 Choosing Adaptation](../labs/1101-choosing-adaptation.md)
- [1002 Metrics And Human Judgment](../labs/1002-metrics-and-human-judgment.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
