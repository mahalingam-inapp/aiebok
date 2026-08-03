# Jobs To Be Done

**Purpose:** Reference card for **jobs to be done** used across AIEBOK books and knowledge areas.

## Core explanation

Jobs-to-be-done frames what users hire a product to accomplish, not which technology it uses. AI fits when it improves the job outcome measurably.

## Example

Users hire expense tool to 'get reimbursed fast', not to 'chat with AI'.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Write job statement and success metric independent of model choice.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare jobs to be done against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baseline Workflow](../../concepts/cards/baseline-workflow.md)
- [Feasibility](../../concepts/cards/feasibility.md)
- [Success Metrics](../../concepts/cards/success-metrics.md)
- [User Research](../../concepts/cards/user-research.md)

## Related chapters

- [01 Discovering The Right Problem](../../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
