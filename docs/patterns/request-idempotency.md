# Request Idempotency

## Context

Duplicate agent or API calls must not double-charge or double-write.

## Solution

Idempotency keys on side-effect tools.

## Consequences

Safer retries. Key storage overhead.

## Do not use when

Read-only idempotent reads only.
