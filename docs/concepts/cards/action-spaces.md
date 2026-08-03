# Action Spaces

**Purpose:** Reference card for **action spaces** used across AIEBOK books and knowledge areas.

## Core explanation

Action spaces define allowed agent operations—click, type, scroll, API call—with granularity affecting reliability.

## Example

Semantic actions ('open_settings') beat raw coordinates when UI reskins change layout.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare success rate semantic versus coordinate actions after UI theme change.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare action spaces against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Computer Use](../../concepts/cards/computer-use.md)
- [Recovery](../../concepts/cards/recovery.md)
- [Robotics Interfaces](../../concepts/cards/robotics-interfaces.md)
- [Visual Grounding](../../concepts/cards/visual-grounding.md)

## Related chapters

- [04 Computer Use And Embodied Action](../../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
