# Ai Coding Agents

**Purpose:** Reference card for **ai coding agents** used across AIEBOK books and knowledge areas.

## Core explanation

AI coding agents autonomously edit repositories given goals, tools, and constraints. They amplify throughput but require specs, tests, and human review.

## Example

Agent implements feature branch with tests; human reviews diff before merge.

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

Track defect density and review time per agent-generated PR versus human-only.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare ai coding agents against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Code Review](../../concepts/cards/code-review.md)
- [Context Files](../../concepts/cards/context-files.md)
- [Repo Instructions](../../concepts/cards/repo-instructions.md)
- [Skills](../../concepts/cards/skills.md)

## Related chapters

- [03 Ai Native Development Workflow](../../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
