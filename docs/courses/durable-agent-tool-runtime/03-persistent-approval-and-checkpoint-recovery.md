# Persistent approval and checkpoint recovery

[Durable Agent Runtime and MCP](index.md) · Pause, recover and replay · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Persist a proposal and its approval against a payload fingerprint, then reopen the runtime.

## How it works

Persist pending work before waiting for a reviewer. Bind approval to the specific proposal so a modified payload needs review. On restart, reconstruct the next permitted transition from stored state.

## Worked example

A reviewer approves a note for meeting M1. Editing the text after review changes its fingerprint, so the previous approval no longer applies.

## Try it yourself

Reopen the SQLite store after creating a proposal. Verify that pending work stays pending and compare a mismatched approval.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The record survives a restart and the wrong fingerprint leaves it awaiting approval.

## Continue

[← Previous lecture](02-tool-authorization-and-argument-validation.md) · [Course outline](index.md) · [Next lecture →](04-idempotent-execution-and-decision-traces.md)
