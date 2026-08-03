# Abstention

**Purpose:** Reference card for **abstention** used across AIEBOK books and knowledge areas.

## Core explanation

Abstention lets a system refuse or defer when confidence is insufficient, routing cases to humans or safer paths. It prevents forced wrong answers on ambiguous inputs.

## Example

A benefits bot abstains on incomplete forms instead of guessing eligibility that triggers appeals.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure coverage (non-abstain rate) versus accuracy on handled cases and set abstention to hit a risk target.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare abstention against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Answer Validation](../../concepts/cards/answer-validation.md)
- [Calibration](../../concepts/cards/calibration.md)
- [Citation Precision](../../concepts/cards/citation-precision.md)
- [Decision Thresholds](../../concepts/cards/decision-thresholds.md)

## Related chapters

- [06 Engineering With Uncertainty](../../books/01-foundations-of-intelligence/06-engineering-with-uncertainty.md)
- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
