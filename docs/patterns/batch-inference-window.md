# Batch Inference Window

## Context

Accumulate requests for efficient GPU batches.

## Solution

Micro-batch within latency SLO.

## Consequences

Higher throughput. Tail latency.

## Do not use when

Strict sub-second SLAs.
