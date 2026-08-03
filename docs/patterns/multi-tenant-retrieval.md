# Multi-Tenant Retrieval

## Context

Isolate retrieval indexes and ACLs per tenant.

## Solution

Filter every query by tenant and role metadata.

## Consequences

Prevents cross-tenant leakage. Index duplication and ops cost.

## Do not use when

Single-tenant internal tools.
