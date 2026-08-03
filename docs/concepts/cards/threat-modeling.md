# Threat Modeling

**Purpose:** Reference card for **threat modeling** used across AIEBOK books and knowledge areas.

## Core explanation

Threat modeling systematically identifies assets, adversaries, and attack paths for AI systems—STRIDE, attack trees adapted for LLM risks.

## Example

Diagram data flow from user → retrieval → model → tools noting untrusted inputs.

## When to use

Use for any system combining untrusted user content, tools, or external retrieval.

## When not to use

Do not treat a single prompt rule as sufficient without tests and monitoring.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Produce threat model doc with mitigations mapped to each high-severity threat.

## Common failure modes

- Prompt injection via retrieved or pasted content
- Tool abuse exfiltrating secrets
- Missing authorization on retrieval paths

## Trade-offs

No mechanism is universal. Compare threat modeling against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Exfiltration](../../concepts/cards/data-exfiltration.md)
- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Sandboxing](../../concepts/cards/sandboxing.md)
- [Tool Abuse](../../concepts/cards/tool-abuse.md)

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
