# Map–Reduce LLM

## Context

Split large inputs, process chunks, merge results.

## Solution

Map per chunk; reduce with structured merge.

## Consequences

Handles long corpora. Merge errors and cost.

## Do not use when

Input fits context.
