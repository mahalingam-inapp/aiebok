# Slices

**Purpose:** Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/slices.md).

## Why this exists

Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure.

## Core intuition

95% overall accuracy can mask 60% on enterprise accounts.

## Mechanics

1. Define the decision or system stage where slices applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Report metrics on three production slices with separate release thresholds.

## Code practice

Run `python labs/1001-evaluation-as-requirements/main.py` from the repository root.

## When to use

Use before every release, model swap, prompt change, or retrieval index migration.

## When not to use

Skip aggregate-only metrics when slices or safety cases can hide regressions.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Common misconceptions

- Fluent language implies reliable behavior.
- One benchmark score generalizes to your product.
- Adding a model call is the same as adding a feature.

## Trade-offs

Slices improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: offline accuracy. Today: slice-based gates and LLM judges with calibration. Tomorrow: continuous eval from production feedback. The durable principle is measuring what users and risk owners care about.
