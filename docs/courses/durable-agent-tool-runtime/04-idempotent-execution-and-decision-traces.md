# Idempotent execution and decision traces

[Durable Agent Runtime and MCP](index.md) · Pause, recover and replay · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Commit a local effect exactly once across retries and distinguish external effects.

## How it works

Record the action and its state transition in the same transaction for a local database effect. A retry can then find the completed record. A remote effect needs its own idempotency contract or a reconciliation process.

## Worked example

The worker restarts after saving an approved agenda note and before returning success. The next attempt reports the existing completion.

## Try it yourself

Reopen the store again and replay the approved action. Check the persistent effect count and trace.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The replay reports the existing result and there is one note. Explain why this guarantee would change for a remote calendar API.

## Continue

[← Previous lecture](03-persistent-approval-and-checkpoint-recovery.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
