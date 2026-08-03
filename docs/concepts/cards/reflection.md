# Reflection

**Purpose:** Reference card for **reflection** used across AIEBOK books and knowledge areas.

## Core explanation

Reflection lets agents critique recent actions and adjust strategy—retry, replan, or escalate. Without reflection, loops repeat the same failing action.

## Example

After tool 403, reflect and switch to read-only search instead of retrying delete.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Count reflection-triggered strategy changes versus blind retries on failure injection suite.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare reflection against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Budgets](../../concepts/cards/budgets.md)
- [Plan Act Observe](../../concepts/cards/plan-act-observe.md)
- [State](../../concepts/cards/state.md)
- [Termination](../../concepts/cards/termination.md)

## Related chapters

- [02 The Agent Loop](../../books/08-agent-systems/02-the-agent-loop.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
