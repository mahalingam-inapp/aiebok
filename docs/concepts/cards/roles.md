# Roles

**Purpose:** Reference card for **roles** used across AIEBOK books and knowledge areas.

## Core explanation

Roles—system, user, assistant, tool—label message provenance and expected behavior in chat APIs. Misassigned roles confuse models about who said what.

## Example

Putting user text in the system role can unintentionally elevate it to trusted policy.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Swap roles on ten prompts and measure compliance change on a fixed eval set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare roles against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Constraints](../../concepts/cards/constraints.md)
- [Delimiters](../../concepts/cards/delimiters.md)
- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Instruction Hierarchy](../../concepts/cards/instruction-hierarchy.md)

## Related chapters

- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
