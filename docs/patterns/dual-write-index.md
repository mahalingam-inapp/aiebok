# Dual-Write Index

## Context

Write new and old indexes during embedding migration.

## Solution

Query both; compare; cutover with flag.

## Consequences

Safe migrations. Double write cost.

## Do not use when

No index migrations.
