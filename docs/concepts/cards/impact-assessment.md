# Impact Assessment

**Purpose:** Reference card for **impact assessment** used across AIEBOK books and knowledge areas.

## Core explanation

Impact assessment evaluates consequences of deploying AI on people, rights, and society before high-risk launch.

## Example

Automated hiring tool requires assessment of bias, appeal process, and human override.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Complete assessment template with sign-offs from legal, security, and product.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare impact assessment against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fairness](../../concepts/cards/fairness.md)
- [Human Oversight](../../concepts/cards/human-oversight.md)
- [Privacy](../../concepts/cards/privacy.md)
- [Transparency](../../concepts/cards/transparency.md)

## Related chapters

- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
