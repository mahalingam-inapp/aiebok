# Hybrid Retrieval

## Context

Combine lexical and dense retrievers when queries mix identifiers and paraphrases.

## Solution

Use reciprocal rank fusion or learned reranking after dual retrieval.

## Consequences

Better recall across query types. Extra latency, index complexity, tuning burden.

## Do not use when

Single-method retrieval suffices for uniform query distribution.
