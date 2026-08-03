# Best Of N

**Purpose:** Reference card for **best of n** used across AIEBOK books and knowledge areas.

## Core explanation

Best-of-N generates N candidates and selects the best by a scorer or verifier. Quality rises with N but so do cost and latency.

## Example

Generate ten JSON plans; pick the one passing all schema and dependency checks.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Plot task success versus N and identify diminishing returns knee.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare best of n against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Critique](../../concepts/cards/critique.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
- [Tests](../../concepts/cards/tests.md)
- [Verifiers](../../concepts/cards/verifiers.md)

## Related chapters

- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
