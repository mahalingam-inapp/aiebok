# Logits

**Purpose:** Reference card for **logits** used across AIEBOK books and knowledge areas.

## Core explanation

Logits are raw pre-softmax scores over the vocabulary for the next token. Decoding policies—temperature, top-k—operate on logits before sampling.

## Example

Inspecting logits reveals whether the model hesitates between two equally likely tokens.

## Evidence of understanding

Log top-5 logits for ten prompts and verify sampling changes when temperature increases.

## Trade-offs

No mechanism is universal. Compare logits against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
