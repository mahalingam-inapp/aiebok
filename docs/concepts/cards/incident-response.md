# Incident Response

**Purpose:** Reference card for **incident response** used across AIEBOK books and knowledge areas.

## Core explanation

Incident response defines detect, triage, mitigate, communicate, and postmortem for AI failures—hallucination harm, data leak, outage.

## Example

Kill switch disables feature flag within 5 minutes of P0 safety incident.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run tabletop exercise quarterly; measure time to mitigation in drill.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare incident response against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Inventory](../../concepts/cards/ai-inventory.md)
- [Audit Evidence](../../concepts/cards/audit-evidence.md)
- [Model Cards](../../concepts/cards/model-cards.md)
- [Risk Tiers](../../concepts/cards/risk-tiers.md)

## Related chapters

- [06 Governance And Assurance](../../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
