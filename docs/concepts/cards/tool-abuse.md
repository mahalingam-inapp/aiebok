# Tool Abuse

**Purpose:** Reference card for **tool abuse** used across AIEBOK books and knowledge areas.

## Core explanation

Tool abuse exploits excessive permissions—delete, send email, SQL write—through manipulated agent behavior.

## Example

Agent tricked into mass email via send_campaign tool with broad scope.

## When to use

Use when tasks require multi-step decisions, tool use, or recovery across variable inputs.

## When not to use

Skip when a deterministic workflow with fixed steps is clearer and safer.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Bound steps, cost, tools, and human approval for side effects.

## Evidence of understanding

Apply least privilege per tool; fuzz adversarial prompts expecting zero abusive executions.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool abuse against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Exfiltration](../../concepts/cards/data-exfiltration.md)
- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Sandboxing](../../concepts/cards/sandboxing.md)
- [Threat Modeling](../../concepts/cards/threat-modeling.md)

## Related chapters

- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
