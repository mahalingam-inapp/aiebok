# Distillation

**Purpose:** Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/distillation.md).

## Why this exists

Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed.

## Core intuition

Student classifier matches teacher on 95% of eval at 5× lower latency.

## Mechanics

1. Define the decision or system stage where distillation applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure student versus teacher gap on full eval and acceptable degradation threshold.

## Code practice

Run `python labs/1102-post-training-methods/main.py` from the repository root.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Common misconceptions

- Fluent language implies reliable behavior.
- One benchmark score generalizes to your product.
- Adding a model call is the same as adding a feature.

## Trade-offs

Distillation improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: research prototypes. Today: measured production systems with eval gates. Tomorrow: tighter integration with enterprise governance. The durable principle is engineering under uncertainty with evidence.
