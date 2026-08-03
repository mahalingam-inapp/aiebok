# Instruction Conflict

**Purpose:** Reference card for **instruction conflict** used across AIEBOK books and knowledge areas.

## Core explanation

Instruction conflict occurs when system, developer, user, or retrieved text give incompatible directives. Resolution policy must be explicit and tested.

## Example

User asks to bypass safety; system forbids it—the system policy must win consistently.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Catalog ten conflict scenarios and measure compliance with documented precedence rules.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare instruction conflict against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Authorization](../../concepts/cards/authorization.md)
- [Context Poisoning](../../concepts/cards/context-poisoning.md)
- [Prompt Injection](../../concepts/cards/prompt-injection.md)
- [Provenance](../../concepts/cards/provenance.md)

## Related chapters

- [05 Context Failure And Security](../../books/05-prompt-and-context-engineering/05-context-failure-and-security.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
