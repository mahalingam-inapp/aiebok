# Tool Registry

**Purpose:** Reference card for **tool registry** used across AIEBOK books and knowledge areas.

## Core explanation

Tool registry catalogs approved agent tools with schemas, owners, and security review status.

## Example

Registry entry for create_jira_ticket includes schema v2 and pentest date.

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

Agents may only bind tools present in registry with current approval.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool registry against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Gateways](../../concepts/cards/ai-gateways.md)
- [Model Catalog](../../concepts/cards/model-catalog.md)
- [Platform Engineering](../../concepts/cards/platform-engineering.md)
- [Shared Retrieval](../../concepts/cards/shared-retrieval.md)

## Related chapters

- [01 Enterprise Ai Building Blocks](../../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
