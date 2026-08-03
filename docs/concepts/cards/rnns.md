# Rnns

**Purpose:** Reference card for **rnns** used across AIEBOK books and knowledge areas.

## Core explanation

Recurrent neural networks process sequences step by step, maintaining hidden state across time. Serial computation limits parallel training and long-range credit assignment.

## Example

Character-level RNN language models learn spelling but struggle with paragraph-level coherence.

## Evidence of understanding

Measure training steps/sec versus transformer on the same sequence length.

## Trade-offs

No mechanism is universal. Compare rnns against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
