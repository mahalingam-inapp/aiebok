# Technology Forecasting

**Purpose:** Reference card for **technology forecasting** used across AIEBOK books and knowledge areas.

## Core explanation

Technology forecasting estimates when emerging capabilities become production-ready using evidence tiers and uncertainty bounds.

## Example

Estimate computer-use reliability for your UI stack as low/med/high with dated reassessment.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Quarterly frontier review updates confidence levels with new reproductions, not headlines.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare technology forecasting against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ablations](../../concepts/cards/ablations.md)
- [Benchmarks](../../concepts/cards/benchmarks.md)
- [Primary Sources](../../concepts/cards/primary-sources.md)
- [Reproduction](../../concepts/cards/reproduction.md)

## Related chapters

- [06 How To Track The Frontier](../../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
