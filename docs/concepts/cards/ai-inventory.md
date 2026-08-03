# Ai Inventory

**Purpose:** Reference card for **ai inventory** used across AIEBOK books and knowledge areas.

## Core explanation

AI inventory catalogs models, datasets, prompts, and features with owners, risk tier, and dependencies. You cannot govern what you cannot find.

## Example

Registry lists prod chatbot v3, embedding model e5-v2, fine-tune data v1.4 with owners.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Quarterly audit: every production AI surface appears in inventory with current owner.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare ai inventory against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Audit Evidence](../../concepts/cards/audit-evidence.md)
- [Incident Response](../../concepts/cards/incident-response.md)
- [Model Cards](../../concepts/cards/model-cards.md)
- [Risk Tiers](../../concepts/cards/risk-tiers.md)

## Related chapters

- [06 Governance And Assurance](../../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
