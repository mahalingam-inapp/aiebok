# Canary cohorts and staged gates

[AI Reliability and Release Engineering](index.md) · Release and recover · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Use predeclared coverage, burn, latency, and cost thresholds to approve or hold a rollout.

## How it works

Keep stable and candidate traffic separately attributed and compare them over a defined window. A gate checks sample size, the critical failures, and cost before expanding. Report the exact gate that stops the rollout.

## Worked example

A cheaper candidate misses the quality and latency gates during a 10% cohort. Pause that version and continue serving stable traffic.

## Try it yourself

Run a healthy and an unhealthy canary. Relax one gate and inspect which other condition still blocks promotion.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A canary passes only after all required evidence conditions pass. A low-cost result still needs adequate reliability.

## Continue

[← Previous lecture](02-stage-traces-and-failure-localization.md) · [Course outline](index.md) · [Next lecture →](04-rollback-verification-and-incident-review.md)
