# Batch Embed Pipeline

## Context

Embed documents in offline batches.

## Solution

Queue docs; batch embed; atomic index swap.

## Consequences

Cost efficient. Ingest lag.

## Do not use when

Real-time ingest required.
