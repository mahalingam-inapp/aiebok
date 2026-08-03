# Checkpoints

**Purpose:** Reference card for **checkpoints** used across AIEBOK books and knowledge areas.

## Core explanation

Checkpoints persist durable agent state so interrupted runs resume without repeating side effects.

## Example

After approval gate, checkpoint stores pending payment until human approves, then continues.

## Evidence of understanding

Kill run mid-loop, restore checkpoint, verify idempotent tools are not duplicated.

## Trade-offs

No mechanism is universal. Compare checkpoints against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
