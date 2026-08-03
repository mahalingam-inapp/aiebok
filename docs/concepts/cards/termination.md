# Termination

**Purpose:** Reference card for **termination** used across AIEBOK books and knowledge areas.

## Core explanation

Termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Without them, systems loop indefinitely.

## Example

Stop after five tool calls, success, or three consecutive no-progress iterations.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify 100% of test runs halt within max_steps and document stop reason distribution.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare termination against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Backtracking](../../concepts/cards/backtracking.md)
- [Budgets](../../concepts/cards/budgets.md)
- [Decomposition](../../concepts/cards/decomposition.md)
- [Heuristics](../../concepts/cards/heuristics.md)

## Related chapters

- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
