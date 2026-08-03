# Permissions

**Purpose:** Reference card for **permissions** used across AIEBOK books and knowledge areas.

## Core explanation

Permissions bind tools and data access to authenticated identities and roles. Models must not bypass authorization by guessing URLs or parameters.

## Example

delete_user tool requires admin role verified server-side, not in the prompt.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Attempt privileged tool calls as low-privilege identity and expect denial.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare permissions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Function Calling](../../concepts/cards/function-calling.md)
- [Idempotency](../../concepts/cards/idempotency.md)
- [Timeouts](../../concepts/cards/timeouts.md)
- [Tool Schemas](../../concepts/cards/tool-schemas.md)

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
