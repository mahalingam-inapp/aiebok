# N Grams

**Purpose:** Reference card for **n grams** used across AIEBOK books and knowledge areas.

## Core explanation

N-gram models predict tokens from local history of n−1 prior tokens—simple, fast, and limited to short context. They remain baselines for compression and sanity checks.

## Example

A trigram model captures 'New York' but not dependencies spanning whole paragraphs.

## Evidence of understanding

Compare perplexity of n-gram versus small neural LM on the same held-out corpus.

## Trade-offs

No mechanism is universal. Compare n grams against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
