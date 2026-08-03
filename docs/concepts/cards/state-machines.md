# State Machines

**Purpose:** Reference card for **state machines** used across AIEBOK books and knowledge areas.

## Core explanation

State machines model allowed statuses and transitions explicitly, making illegal steps unrepresentable. They clarify where agents pause, resume, or terminate.

## Example

Ticket automation states: open → pending_approval → resolved with defined transition triggers.

## Evidence of understanding

Draw state diagram and verify code rejects all undefined transitions in tests.

## Trade-offs

No mechanism is universal. Compare state machines against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
