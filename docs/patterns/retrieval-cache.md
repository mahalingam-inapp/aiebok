# Retrieval Cache

## Context

Cache retrieval results for hot queries.

## Solution

TTL cache keyed by query+filters.

## Consequences

Latency savings. Stale answers.

## Do not use when

Highly dynamic corpora.
