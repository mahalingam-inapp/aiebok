# Json Schema

**Purpose:** JSON Schema declares required fields, types, and constraints that validators enforce after model generation.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/json-schema.md).

## Why this exists

JSON Schema declares required fields, types, and constraints that validators enforce after model generation. It turns free-form text into typed data boundaries.

## Core intuition

Rejecting payloads where 'total' is a string prevents silent accounting errors from plausible JSON.

## Mechanics

1. Define the decision or system stage where json schema applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Validate three intentionally invalid payloads and confirm distinct error reasons.

## Code practice

Run `python labs/0502-structured-generation/main.py` from the repository root.

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

Json Schema improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: research prototypes. Today: measured production systems with eval gates. Tomorrow: tighter integration with enterprise governance. The durable principle is engineering under uncertainty with evidence.
