# Portable Interfaces

**Purpose:** Reference card for **portable interfaces** used across AIEBOK books and knowledge areas.

## Core explanation

Portable interfaces—OpenAI-compatible APIs, OTel traces, standard embedding dims—reduce lock-in across clouds.

## Example

Gateway speaks OpenAI schema; backends swap Bedrock, Azure, or vLLM without client changes.

## Evidence of understanding

Migrate one backend in staging with zero client SDK changes verified by integration tests.

## Trade-offs

No mechanism is universal. Compare portable interfaces against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
