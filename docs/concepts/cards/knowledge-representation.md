# Knowledge Representation

**Purpose:** Reference card for **knowledge representation** used across AIEBOK books and knowledge areas.

## Core explanation

Knowledge representation chooses how facts, relations, and uncertainty are stored—graphs, frames, schemas, or vectors. The representation determines what queries and updates are cheap or hard.

## Example

Modeling product compatibility as a graph makes 'works-with' queries fast; flattening to text loses compositional structure.

## Evidence of understanding

Run three query types on the same facts in two representations and compare answer latency and correctness.

## Trade-offs

No mechanism is universal. Compare knowledge representation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
