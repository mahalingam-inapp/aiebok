# Fine Tuning

**Purpose:** Reference card for **fine tuning** used across AIEBOK books and knowledge areas.

## Core explanation

Fine-tuning adapts pretrained weights with supervised or preference data when prompts and RAG cannot stabilize behavior. It trades generality and ops simplicity for targeted changes.

## Example

Support tone and escalation policy may need SFT when prompts drift across thousands of ticket types.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare fine-tuned and prompt-only models on held-out behavioral eval with rollback plan.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare fine tuning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Behavior Versus Knowledge](../../concepts/cards/behavior-versus-knowledge.md)
- [Grounding](../../concepts/cards/grounding.md)
- [Knowledge Freshness](../../concepts/cards/knowledge-freshness.md)
- [Model Selection](../../concepts/cards/model-selection.md)

## Related chapters

- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)
- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
