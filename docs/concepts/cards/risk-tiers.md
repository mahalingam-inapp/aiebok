# Risk Tiers

**Purpose:** Reference card for **risk tiers** used across AIEBOK books and knowledge areas.

## Core explanation

Risk tiers classify AI systems by potential harm—low, medium, high—driving eval depth, approval path, and monitoring.

## Example

Internal summarization is tier 1; automated credit decision is tier 3 with full gate package.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Assign tier per system; verify tier-3 systems have required controls before deploy.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare risk tiers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Inventory](../../concepts/cards/ai-inventory.md)
- [Audit Evidence](../../concepts/cards/audit-evidence.md)
- [Incident Response](../../concepts/cards/incident-response.md)
- [Model Cards](../../concepts/cards/model-cards.md)

## Related chapters

- [06 Governance And Assurance](../../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
