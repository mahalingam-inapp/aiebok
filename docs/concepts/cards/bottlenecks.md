# Bottlenecks

**Purpose:** Reference card for **bottlenecks** used across AIEBOK books and knowledge areas.

## Core explanation

Information bottlenecks force compressive representations—fixed-size context vectors or limited bandwidth channels. They create trade-offs between memory and expressiveness.

## Example

Early seq2seq used a single context vector for entire sentences, losing detail on long inputs.

## Evidence of understanding

Compare output quality on 50-token versus 500-token inputs through a fixed bottleneck.

## Trade-offs

No mechanism is universal. Compare bottlenecks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
