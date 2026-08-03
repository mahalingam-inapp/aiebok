# Human Evaluation

**Purpose:** Human evaluation labels outputs quality when automation cannot capture nuance or safety.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/human-evaluation.md).

## Why this exists

Human evaluation labels outputs quality when automation cannot capture nuance or safety. Design for rater training, agreement, and throughput.

## Core intuition

Lawyers label contract summaries for legal accuracy on 50 cases monthly.

## Mechanics

1. Define the decision or system stage where human evaluation applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Track inter-rater agreement and adjudicate disagreements with gold committee.

## Code practice

Run `python labs/1002-metrics-and-human-judgment/main.py` from the repository root.

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

Human Evaluation improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: offline accuracy. Today: slice-based gates and LLM judges with calibration. Tomorrow: continuous eval from production feedback. The durable principle is measuring what users and risk owners care about.
