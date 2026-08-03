# Computer Use

**Purpose:** Reference card for **computer use** used across AIEBOK books and knowledge areas.

## Core explanation

Computer use agents perceive screens and emit mouse/keyboard actions to complete software tasks.

## Example

Agent fills expense form in internal web app from receipt image with confirmation gates.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Task success rate on sandboxed UI benchmark with zero unauthorized actions.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare computer use against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Action Spaces](../../concepts/cards/action-spaces.md)
- [Recovery](../../concepts/cards/recovery.md)
- [Robotics Interfaces](../../concepts/cards/robotics-interfaces.md)
- [Visual Grounding](../../concepts/cards/visual-grounding.md)

## Related chapters

- [04 Computer Use And Embodied Action](../../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
