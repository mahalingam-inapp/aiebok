# Control

**Purpose:** Reference card for **control** used across AIEBOK books and knowledge areas.

## Core explanation

Control mechanisms—approvals, rate limits, tool allowlists— constrain agent behavior within safe envelopes. Control is designed, not emergent from prompts alone.

## Example

Payments above $500 require human approval even if the agent recommends proceed.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Attempt forbidden actions in red-team tests and verify control layer blocks 100%.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare control against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Agency](../../concepts/cards/agency.md)
- [Autonomy](../../concepts/cards/autonomy.md)
- [State Machines](../../concepts/cards/state-machines.md)
- [Workflows](../../concepts/cards/workflows.md)

## Related chapters

- [01 Agent Or Workflow](../../books/08-agent-systems/01-agent-or-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
