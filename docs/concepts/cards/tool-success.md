# Tool Success

**Purpose:** Reference card for **tool success** used across AIEBOK books and knowledge areas.

## Core explanation

Tool success rate tracks correct schema, auth, execution, and useful results from tool calls. It isolates integration failures from model reasoning.

## Example

60% tool success with high answer quality still blocks reliable agents.

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

Log tool error taxonomy—validation, timeout, 403—and set minimum success rate gate.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Trade-offs

No mechanism is universal. Compare tool success against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Component Evals](../../concepts/cards/component-evals.md)
- [End To End Evals](../../concepts/cards/end-to-end-evals.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)
- [Retrieval Metrics](../../concepts/cards/retrieval-metrics.md)

## Related chapters

- [03 Evaluation By System Stage](../../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
