# Spec-to-Production AI Feature

## Goal

Discovery through spec, implementation, eval, and rollout.

## Overview

Take an AI feature from problem discovery through executable spec, implementation, eval, and gradual rollout. Each stage produces artifacts that gate the next, reducing rework and unmeasured launches.

## Architecture

The workflow starts with a problem brief tied to user evidence, not model capability. An executable spec defines inputs, outputs, eval cases, and non-goals. Implementation sits behind a feature flag with eval-gated CI. Rollout stages traffic while comparing slice metrics to a control.

## Prerequisites

Complete the matching [guided book](../books/09-ai-software-and-product-engineering/index.md) and related labs.

## Build phases

### 1. Problem brief

**Goal:** Validate that the problem warrants an AI solution.

**Steps:**
   - Document user pain with quotes, frequency, and cost of status quo.
   - List non-AI alternatives considered and why insufficient.
   - Define success metrics tied to user outcomes, not model scores alone.
   - Get stakeholder sign-off before spec work begins.

**Acceptance:**
   - Brief cites at least three user evidence points or support tickets.
   - Success metric has baseline measurement from current workflow.
   - Explicit non-goals prevent scope creep.

   **Commands:**

   ```bash
   python specs/new_brief.py --template templates/problem_brief.md --out docs/briefs/feature-x.md
   ```
### 2. Executable spec

**Goal:** Write a testable spec with eval cases and acceptance thresholds.

**Steps:**
   - Specify API contract, error modes, and latency budget.
   - Attach eval cases derived from brief scenarios.
   - Define acceptance thresholds per slice and abstention policy.
   - Review spec with eng, product, and eval owners.

**Acceptance:**
   - Every acceptance criterion maps to an automated or scripted check.
   - Spec includes rollback and fallback behavior.
   - Review recorded with approvers named in spec header.

   **Commands:**

   ```bash
   python specs/validate.py --spec specs/feature-x.yaml
   python eval/run_from_spec.py --spec specs/feature-x.yaml --out reports/spec_eval.json
   ```
### 3. Feature flag rollout

**Goal:** Ship gradually with measurement and fast rollback.

**Steps:**
   - Implement feature behind flag default-off in production config.
   - Run spec evals in CI; block merge on threshold failures.
   - Roll out 1% → 10% → 50% → 100% with soak periods.
   - Compare treatment vs control on brief success metrics and eval proxies.

**Acceptance:**
   - Flag off restores baseline behavior within one config push.
   - Rollout pauses automatically if error rate or primary metric regresses.
   - Final report links brief, spec, eval results, and rollout timeline.

   **Commands:**

   ```bash
   python deploy/feature_flag.py --enable feature-x --percent 5 --dry-run
   python eval/compare_rollout.py --metric support_deflection --control control --treatment feature-x
   ```

## Troubleshooting

- Spec evals pass but users unhappy: success metrics in brief diverged from eval proxies; realign.
- Rollout stuck at low percent: insufficient traffic for slices; extend soak or widen cohort.
- Flag toggles wrong environment: namespace flags per env and add startup log of active flags.
- Scope creep mid-implementation: enforce non-goals in spec review and reject untracked cases.

## Related patterns

- [Spec Driven Ai Feature](../patterns/spec-driven-ai-feature.md)
- [Feature Flag Model](../patterns/feature-flag-model.md)
- [Eval Gated Release](../patterns/eval-gated-release.md)
- [Online Canary](../patterns/online-canary.md)

## Related labs

- [0901 Discovering The Right Problem](../labs/0901-discovering-the-right-problem.md)
- [0902 Specification Driven Development](../labs/0902-specification-driven-development.md)
- [0906 Experiments Adoption And Value](../labs/0906-experiments-adoption-and-value.md)
- [0904 Testing Ai Systems](../labs/0904-testing-ai-systems.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
