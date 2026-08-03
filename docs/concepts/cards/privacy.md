# Privacy

**Purpose:** Reference card for **privacy** used across AIEBOK books and knowledge areas.

## Core explanation

Privacy limits collection, retention, and exposure of personal data in training, logs, and outputs. GDPR and similar laws define user rights.

## Example

Support logs must redact credit card numbers; retention capped at 90 days.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run PII scanner on logs and outputs; zero high-severity findings before release.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare privacy against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fairness](../../concepts/cards/fairness.md)
- [Human Oversight](../../concepts/cards/human-oversight.md)
- [Impact Assessment](../../concepts/cards/impact-assessment.md)
- [Transparency](../../concepts/cards/transparency.md)

## Related chapters

- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
