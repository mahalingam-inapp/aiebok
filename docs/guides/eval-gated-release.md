# Eval-Gated Release Pipeline

## Goal

CI harness with slices, thresholds, and rollback evidence.

## Overview

Wire evaluation into CI so no model, prompt, or retrieval change ships without passing slice-aware thresholds. Canary plans and rollback evidence make releases  reversible when live metrics diverge.

## Architecture

The release pipeline runs gold-case evals, computes slice metrics, and compares against baselines stored per environment. A gate service returns pass/fail with reason codes. Approved releases attach evidence bundles. Canary configuration routes a small traffic fraction to the candidate while comparing live slice metrics.

## Prerequisites

Complete the matching [guided book](../books/10-evaluation-safety-and-governance/index.md) and related labs.

## Build phases

### 1. Gold cases

**Goal:** Maintain authoritative eval cases tied to product requirements.

**Steps:**
   - Map each requirement to at least one gold case with expected behavior.
   - Version gold cases; require review for additions or semantic edits.
   - Include adversarial and regression cases for past production incidents.
   - Store cases as JSONL with slice tags and severity levels.

**Acceptance:**
   - Gold suite covers all P0 requirements documented in the spec.
   - Case edits require PR review and version bump in manifest.
   - Adversarial subset runs on every CI build.

   **Commands:**

   ```bash
   python eval/validate_gold.py --path data/gold_cases.jsonl
   python eval/run_gold.py --cases data/gold_cases.jsonl --out reports/gold.json
   ```
### 2. Slice metrics

**Goal:** Measure quality per segment, not only aggregate averages.

**Steps:**
   - Define slices: domain, language, user tier, query length, data vintage.
   - Compute metrics per slice: accuracy, citation precision, abstention rate.
   - Compare candidate vs baseline with minimum sample size guards.
   - Highlight slices with >2pt regression in the CI summary.

**Acceptance:**
   - Report includes per-slice metrics with sample counts.
   - Slices with n<5 flagged as low-confidence, not silently ignored.
   - Regression detection configurable per slice severity.

   **Commands:**

   ```bash
   python eval/slice_metrics.py --report reports/gold.json --slices config/slices.yaml
   python eval/diff_baselines.py --candidate reports/gold.json --baseline reports/baseline.json
   ```
### 3. Release gate

**Goal:** Automate pass/fail decisions with auditable reason codes.

**Steps:**
   - Define thresholds per metric and slice in YAML.
   - Implement gate logic: fail on any P0 slice regression or global critical miss.
   - Emit structured pass/fail with reason codes for CI and dashboards.
   - Block merge/deploy when gate fails unless explicit override with ticket.

**Acceptance:**
   - Gate fails closed when eval artifacts missing or malformed.
   - Override path requires documented ticket id and expires after one deploy.
   - Pass/fail JSON archived with git sha and artifact urls.

   **Commands:**

   ```bash
   python eval/release_gate.py --report reports/gold.json --thresholds config/thresholds.yaml
   python eval/release_gate.py --report reports/gold.json --thresholds config/thresholds.yaml --strict
   ```
### 4. Canary plan

**Goal:** Roll out gradually with live metric comparison and rollback triggers.

**Steps:**
   - Document canary stages: 1%, 5%, 25%, 100% with soak durations.
   - Define live metrics to watch: error rate, latency p95, quality proxy.
   - Set automatic rollback triggers tied to slice-specific live dashboards.
   - Write rollback runbook: flag flip, cache invalidation, stakeholder notify.

**Acceptance:**
   - Canary plan linked from release PR and evidence bundle.
   - Rollback executable in under 5 minutes without redeploy.
   - Live dashboard compares canary vs control on matching slices.

   **Commands:**

   ```bash
   python deploy/canary_plan.py --version v1.2.3 --out deploy/canary.yaml
   python deploy/rollback.py --feature new-reranker --dry-run
   ```

## Troubleshooting

- Gate passes but production fails: live metrics differ from offline gold; add production-shadow eval.
- Slice sample too small: merge low-traffic slices or lengthen collection window before gating.
- Flaky LLM-judge scores: calibrate judges on a human-labeled subset and use median-of-three.
- Override culture erodes gate: audit overrides monthly and tie to incident postmortems.

## Related patterns

- [Eval Gated Release](../patterns/eval-gated-release.md)
- [Slice Based Eval](../patterns/slice-based-eval.md)
- [Online Canary](../patterns/online-canary.md)
- [Offline Eval Regression](../patterns/offline-eval-regression.md)

## Related labs

- [1001 Evaluation As Requirements](../labs/1001-evaluation-as-requirements.md)
- [1003 Evaluation By System Stage](../labs/1003-evaluation-by-system-stage.md)
- [1002 Metrics And Human Judgment](../labs/1002-metrics-and-human-judgment.md)
- [1006 Governance And Assurance](../labs/1006-governance-and-assurance.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
