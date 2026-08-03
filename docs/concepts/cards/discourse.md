# Discourse

**Purpose:** Reference card for **discourse** used across AIEBOK books and knowledge areas.

## Core explanation

Discourse connects sentences across turns and documents—coreference, topic continuity, rhetorical structure. Long interactions fail when each turn is processed in isolation.

## Example

'It' in turn three refers to the outage mentioned in turn one only if discourse state is preserved.

## Evidence of understanding

Run a coreference test set and report F1 on pronouns spanning three or more turns.

## Trade-offs

No mechanism is universal. Compare discourse against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
