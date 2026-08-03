# Containers

**Purpose:** Reference card for **containers** used across AIEBOK books and knowledge areas.

## Core explanation

Containers package model servers with dependencies for reproducible deployment across environments.

## Example

Docker image pins CUDA, Python, and model weights hash for prod inference.

## Evidence of understanding

Scan container image for CVEs; block deploy on critical unfixed vulnerabilities.

## Trade-offs

No mechanism is universal. Compare containers against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
