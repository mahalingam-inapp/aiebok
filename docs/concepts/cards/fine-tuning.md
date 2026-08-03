# Fine Tuning

**Purpose:** Reference card for **fine tuning** used across AIEBOK books and knowledge areas.

## Core explanation

Fine-tuning adapts pretrained weights with supervised or preference data when prompts and RAG cannot stabilize behavior. It trades generality and ops simplicity for targeted changes.

## Example

Support tone and escalation policy may need SFT when prompts drift across thousands of ticket types.

## Evidence of understanding

Compare fine-tuned and prompt-only models on held-out behavioral eval with rollback plan.

## Trade-offs

No mechanism is universal. Compare fine tuning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
