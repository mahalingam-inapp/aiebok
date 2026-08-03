# Prompting

**Purpose:** Prompting steers model behavior at inference via instructions and examples without weight updates.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/prompting.md).

## Why this exists

Prompting steers model behavior at inference via instructions and examples without weight updates. It is the fastest iteration path when context fits.

## Core intuition

Adding 'cite sources' instruction improves citation rate without retraining.

## Mechanics

1. Define the decision or system stage where prompting applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare prompt variants on behavioral eval with fixed model weights.

## Code practice

Run `python labs/1101-choosing-adaptation/main.py` from the repository root.

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

Prompting improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: research prototypes. Today: measured production systems with eval gates. Tomorrow: tighter integration with enterprise governance. The durable principle is engineering under uncertainty with evidence.
