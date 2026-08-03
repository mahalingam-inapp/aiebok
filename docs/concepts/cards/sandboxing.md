# Sandboxing

**Purpose:** Reference card for **sandboxing** used across AIEBOK books and knowledge areas.

## Core explanation

Sandboxing isolates code execution, browsing, or file access in restricted environments with network and filesystem limits.

## Example

Python tool runs in container without egress except allowlisted APIs.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Attempt filesystem and network escapes in sandbox test suite monthly.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare sandboxing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Exfiltration](../../concepts/cards/data-exfiltration.md)
- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Threat Modeling](../../concepts/cards/threat-modeling.md)
- [Tool Abuse](../../concepts/cards/tool-abuse.md)

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
