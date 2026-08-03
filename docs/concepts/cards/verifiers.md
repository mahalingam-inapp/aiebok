# Verifiers

**Purpose:** Reference card for **verifiers** used across AIEBOK books and knowledge areas.

## Core explanation

Verifiers check candidate outputs with independent logic—unit tests, schemas, calculators—not the same model that generated them.

## Example

A Python assert verifies JSON plan steps include all required migration phases.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report verifier catch rate on intentionally corrupted candidate outputs.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare verifiers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Best Of N](../../concepts/cards/best-of-n.md)
- [Critique](../../concepts/cards/critique.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
- [Tests](../../concepts/cards/tests.md)

## Related chapters

- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
