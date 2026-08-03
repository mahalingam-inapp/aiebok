# Audit

**Purpose:** Reference card for **audit** used across AIEBOK books and knowledge areas.

## Core explanation

Audit logs record who accessed which models, documents, and tools with immutable retention for compliance.

## Example

Log entry: user, query hash, retrieved doc IDs, model version, timestamp.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Simulate auditor request; produce complete trail for sample user within SLA.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare audit against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authorization](../../concepts/cards/authorization.md)
- [Data Residency](../../concepts/cards/data-residency.md)
- [Identity](../../concepts/cards/identity.md)
- [Multi Tenancy](../../concepts/cards/multi-tenancy.md)

## Related chapters

- [02 Identity Data And Trust Boundaries](../../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
