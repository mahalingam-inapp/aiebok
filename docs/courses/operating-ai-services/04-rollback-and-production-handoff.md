# Rollback and production handoff

[Deploy and Operate an AI Service](index.md) · Release and recover · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Persist a version-pointer rollback and verify it through a local HTTP smoke test.

## How it works

Rollback restores the previous serving version. Keep the decision durable and include it in the operator log. After changing the pointer, send a smoke request through the serving endpoint. In hosted environments, use a managed secret store, readiness checks, and an explicit release owner.

## Worked example

A blocked canary reassigns the production pointer to v1. After reopening its state store, the next request reports v1 and the decision log still contains the rollback.

## Try it yourself

Run rollback, reopen the store, and make a loopback HTTP health and prediction request. Write your runbook with the measurable trigger and post-rollback check.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The version pointer and decision survive reopen. The deployed service reports its baseline version through HTTP.

## Continue

[← Previous lecture](03-canary-evaluation-and-rollout-decisions.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
