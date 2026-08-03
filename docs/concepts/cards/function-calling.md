# Function Calling

**Purpose:** Reference card for **function calling** used across AIEBOK books and knowledge areas.

## Core explanation

Function calling lets models emit structured invocations with typed arguments that runtime code validates and executes.

## Example

Searching internal docs via a read-only tool returns live titles instead of hallucinated links.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Fuzz tool arguments and confirm unauthorized calls fail before side effects.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare function calling against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Idempotency](../../concepts/cards/idempotency.md)
- [Permissions](../../concepts/cards/permissions.md)
- [Timeouts](../../concepts/cards/timeouts.md)
- [Tool Schemas](../../concepts/cards/tool-schemas.md)

## Related chapters

- [04 Tools As Capability Boundaries](../../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
