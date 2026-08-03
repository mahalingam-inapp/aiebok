# Keys

**Purpose:** Reference card for **keys** used across AIEBOK books and knowledge areas.

## Core explanation

Keys are attention projections indexed for lookup—compatible queries receive high weights. Together with values they implement content-addressable memory over sequences.

## Example

A pronoun's query should match keys at its antecedent position for correct coreference routing.

## Evidence of understanding

Mask illegal keys and confirm attention mass stays on permitted positions only.

## Trade-offs

No mechanism is universal. Compare keys against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
