# Temperature

**Purpose:** Reference card for **temperature** used across AIEBOK books and knowledge areas.

## Core explanation

Temperature scales logits before softmax—lower sharpens the distribution (more deterministic), higher flattens it (more random). It is a primary creativity-versus-consistency knob.

## Example

Temperature 0.2 keeps support answers stable; 1.2 increases phrasing variety for marketing copy.

## Evidence of understanding

Plot entropy of next-token distribution versus temperature on a fixed prompt set.

## Trade-offs

No mechanism is universal. Compare temperature against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
