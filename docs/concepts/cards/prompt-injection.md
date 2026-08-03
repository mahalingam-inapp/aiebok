# Prompt Injection

**Purpose:** Reference card for **prompt injection** used across AIEBOK books and knowledge areas.

## Core explanation

Prompt injection embeds hostile instructions in untrusted content that models may follow instead of trusted policy.

## Example

A retrieved page saying 'ignore previous instructions' can redirect a summarizer to exfiltrate secrets.

## Evidence of understanding

Red-team with malicious retrieved text and verify external content is treated as data only.

## Trade-offs

No mechanism is universal. Compare prompt injection against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
