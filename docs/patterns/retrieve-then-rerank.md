# Retrieve Then Rerank

## Context

Fast first-stage retrieval followed by cross-encoder reranking.

## Solution

Retrieve top-N quickly; rerank top-M before generation.

## Consequences

Improved precision@k. Added model call and latency.

## Do not use when

Small corpora where brute-force scoring is cheap.
