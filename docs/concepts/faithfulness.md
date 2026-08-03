# Faithfulness

**Purpose:** Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/faithfulness.md).

## Why this exists

Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions. It is separate from fluency or user satisfaction.

## Core intuition

Correct tone but wrong deductible amount is unfaithful despite readable prose.

## Mechanics

1. Define the decision or system stage where faithfulness applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Use NLI or human rubric on 100 answers; require faithfulness ≥ threshold for release.

## Code practice

Run `python labs/0605-rag-generation-and-citations/main.py` from the repository root.

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

Faithfulness improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: offline accuracy. Today: slice-based gates and LLM judges with calibration. Tomorrow: continuous eval from production feedback. The durable principle is measuring what users and risk owners care about.
