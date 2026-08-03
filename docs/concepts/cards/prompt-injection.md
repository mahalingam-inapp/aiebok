# Prompt Injection

**Purpose:** Reference card for **prompt injection** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt injection embeds hostile instructions in untrusted content that models may follow instead of trusted policy.

## Example

A retrieved page saying 'ignore previous instructions' can redirect a summarizer to exfiltrate secrets.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Red-team with malicious retrieved text and verify external content is treated as data only.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare prompt injection against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authorization](../../concepts/cards/authorization.md)
- [Context Poisoning](../../concepts/cards/context-poisoning.md)
- [Data Exfiltration](../../concepts/cards/data-exfiltration.md)
- [Instruction Conflict](../../concepts/cards/instruction-conflict.md)

## Related chapters

- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)
- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
