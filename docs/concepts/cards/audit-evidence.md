# Audit Evidence

**Purpose:** Reference card for **audit evidence** used across AIEBOK books and knowledge areas.

## Core explanation

Audit evidence collects eval reports, approvals, change logs, and incident records demonstrating controlled AI delivery.

## Example

Release ticket links eval v47 pass, security review, and canary metrics.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Auditor can trace any prod model version to eval artifact and approver within 15 minutes.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare audit evidence against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Inventory](../../concepts/cards/ai-inventory.md)
- [Incident Response](../../concepts/cards/incident-response.md)
- [Model Cards](../../concepts/cards/model-cards.md)
- [Risk Tiers](../../concepts/cards/risk-tiers.md)

## Related chapters

- [06 Governance And Assurance](../../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
