# Cost Quality Curves

**Purpose:** Reference card for **cost quality curves** used across AIEBOK books and knowledge areas.

## Core explanation

Cost-quality curves plot spend—tokens, GPU seconds, API dollars—against task metrics. They guide routing and when to stop adding compute.

## Example

Best-of-N may lift accuracy 2 points for 4× cost—acceptable only above a revenue threshold.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Generate curve points for three strategies and document chosen operating point rationale.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare cost quality curves against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Budgets](../../concepts/cards/budgets.md)
- [Latency](../../concepts/cards/latency.md)
- [Routing](../../concepts/cards/routing.md)
- [Test Time Compute](../../concepts/cards/test-time-compute.md)

## Related chapters

- [06 Reasoning System Economics](../../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
