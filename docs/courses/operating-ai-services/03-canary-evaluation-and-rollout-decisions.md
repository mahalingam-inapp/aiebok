# Canary evaluation and rollout decisions

[Deploy and Operate an AI Service](index.md) · Release and recover · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Compare gated evidence and identify a canary that must pause.

## How it works

A canary is a limited rollout of a labeled version. Define sample requirements, acceptable fallback or error rates, and a latency bound. Evaluate on traffic attributed to the requested version, so fallbacks do not improve the apparent reliability of the failing version.

## Worked example

If the candidate has two failures in ten comparable requests and the maximum is one in ten, pause even when all ten callers received some response.

## Try it yourself

Run the gate with a limited candidate cohort and compare its decision with normal traffic. The notebook uses a loopback request header to select the fixture cohort. In a deployed service, assign cohorts in trusted routing infrastructure.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    An insufficient sample should fail with a coverage reason. A well-sampled unhealthy candidate should fail with the measured rate.

## Continue

[← Previous lecture](02-fallback-trace-fields-and-durable-telemetry.md) · [Course outline](index.md) · [Next lecture →](04-rollback-and-production-handoff.md)
