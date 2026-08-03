# User Research

**Purpose:** Reference card for **user research** used across AIEBOK books and knowledge areas.

## Core explanation

User research observes real workflows, pain points, and workarounds before proposing AI features. It prevents building impressive demos nobody needs.

## Example

Watching support agents copy-paste from three systems reveals integration beats summarization.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document five observed user sessions and map pains to non-AI and AI options.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare user research against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baseline Workflow](../../concepts/cards/baseline-workflow.md)
- [Feasibility](../../concepts/cards/feasibility.md)
- [Jobs To Be Done](../../concepts/cards/jobs-to-be-done.md)
- [Success Metrics](../../concepts/cards/success-metrics.md)

## Related chapters

- [01 Discovering The Right Problem](../../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
