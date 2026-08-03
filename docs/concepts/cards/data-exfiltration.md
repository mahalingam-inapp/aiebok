# Data Exfiltration

**Purpose:** Reference card for **data exfiltration** used across AIEBOK books and knowledge areas.

## Core explanation

Data exfiltration via AI occurs when prompts or tools leak secrets, PII, or restricted docs to unauthorized parties.

## Example

Injection tricking model to dump system prompt or customer list into chat.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Red-team exfil scenarios; verify DLP blocks and zero successful leaks in test.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data exfiltration against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Sandboxing](../../concepts/cards/sandboxing.md)
- [Threat Modeling](../../concepts/cards/threat-modeling.md)
- [Tool Abuse](../../concepts/cards/tool-abuse.md)

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
