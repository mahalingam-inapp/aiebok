# Tenant Rate Limit

## Context

Fair usage across customers on shared models.

## Solution

Token bucket per tenant with burst.

## Consequences

Protects platform. Throttling complaints.

## Do not use when

Single-tenant deployment.
