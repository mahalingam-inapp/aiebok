# Budgets

**Purpose:** Reference card for **budgets** used across AIEBOK books and knowledge areas.

## Core explanation

Budgets cap tokens, tool calls, wall time, or dollars per task or session. Hard budgets prevent runaway agents and make economics predictable.

## Example

A research agent stops after $0.50 API spend or ten tool calls, whichever comes first.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify 100% of runs respect budget caps in stress tests with tempting infinite loops.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare budgets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Cost Quality Curves](../../concepts/cards/cost-quality-curves.md)
- [Latency](../../concepts/cards/latency.md)
- [Plan Act Observe](../../concepts/cards/plan-act-observe.md)
- [Reflection](../../concepts/cards/reflection.md)

## Related chapters

- [06 Reasoning System Economics](../../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md)
- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
