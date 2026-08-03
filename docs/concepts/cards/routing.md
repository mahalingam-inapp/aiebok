# Routing

**Purpose:** Reference card for **routing** used across AIEBOK books and knowledge areas.

## Core explanation

Routing directs requests to models, tools, or strategies by task type, risk, or budget. Routers encode product policy about cheap versus capable paths.

## Example

Simple FAQs route to small model; compliance questions route to audited large model.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Log routing decisions and compare quality and cost versus always-large baseline.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare routing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Approval Gates](../../concepts/cards/approval-gates.md)
- [Budgets](../../concepts/cards/budgets.md)
- [Cost Quality Curves](../../concepts/cards/cost-quality-curves.md)
- [Latency](../../concepts/cards/latency.md)

## Related chapters

- [06 Reasoning System Economics](../../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md)
- [04 Agent Patterns](../../books/08-agent-systems/04-agent-patterns.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
