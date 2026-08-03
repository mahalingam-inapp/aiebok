# Agency

**Purpose:** Reference card for **agency** used across AIEBOK books and knowledge areas.

## Core explanation

Agency is goal-directed action selection in a loop—observe, decide, act—rather than a single model call. It implies autonomy bounded by policy, tools, and termination rules.

## Example

An agent chooses which tool to call next based on observations, unlike a fixed workflow script.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare task completion on variable inputs between scripted workflow and agent with same tools.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare agency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Autonomy](../../concepts/cards/autonomy.md)
- [Control](../../concepts/cards/control.md)
- [State Machines](../../concepts/cards/state-machines.md)
- [Workflows](../../concepts/cards/workflows.md)

## Related chapters

- [01 Agent Or Workflow](../../books/08-agent-systems/01-agent-or-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
