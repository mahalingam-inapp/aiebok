# Eval-Gated Release

## Context

Block release until predefined eval slices pass.

## Solution

CI runs component and end-to-end evals with thresholds.

## Consequences

Safer deployment of probabilistic systems. Slower release cadence; eval maintenance.

## Do not use when

Non-production experiments without user impact.
