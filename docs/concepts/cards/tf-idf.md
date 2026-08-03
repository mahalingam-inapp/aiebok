# Tf Idf

**Purpose:** Reference card for **tf idf** used across AIEBOK books and knowledge areas.

## Core explanation

TF–IDF weights terms by local frequency and inverse document frequency, highlighting discriminative words in sparse retrieval. It is a strong lexical baseline before dense methods.

## Example

Searching 'PTO accrual cap' ranks handbook sections containing rare terms 'accrual' and 'cap' highly.

## Evidence of understanding

Measure recall@10 on 30 keyword-heavy queries against a dense baseline.

## Trade-offs

No mechanism is universal. Compare tf idf against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
