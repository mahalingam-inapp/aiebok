# Model Cards

**Purpose:** Reference card for **model cards** used across AIEBOK books and knowledge areas.

## Core explanation

Model cards document intended use, training data, limitations, metrics, and ethical considerations for a model version.

## Example

Card states model not for legal advice; lists languages supported and known failure modes.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Publish model card link in registry for every production model version.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare model cards against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Inventory](../../concepts/cards/ai-inventory.md)
- [Audit Evidence](../../concepts/cards/audit-evidence.md)
- [Incident Response](../../concepts/cards/incident-response.md)
- [Risk Tiers](../../concepts/cards/risk-tiers.md)

## Related chapters

- [06 Governance And Assurance](../../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
