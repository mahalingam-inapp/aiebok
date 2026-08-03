# Tool Contracts

**Purpose:** Reference card for **tool contracts** used across AIEBOK books and knowledge areas.

## Core explanation

Tool contracts specify schemas, auth, idempotency, errors, and SLAs for each agent tool. They are integration boundaries models depend on.

## Example

search_docs contract promises p95 500ms, max 10 results, ReadScope auth.

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

Contract tests mock failures and verify agent handles each error code.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool contracts against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Acceptance Criteria](../../concepts/cards/acceptance-criteria.md)
- [Evaluation Specs](../../concepts/cards/evaluation-specs.md)
- [Functional Specifications](../../concepts/cards/functional-specifications.md)
- [Prompt Specs](../../concepts/cards/prompt-specs.md)

## Related chapters

- [02 Specification Driven Development](../../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
