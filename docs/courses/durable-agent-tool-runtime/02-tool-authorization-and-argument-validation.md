# Tool authorization and argument validation

[Durable Agent Runtime and MCP](index.md) · Connect and constrain · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Validate caller scope and arguments before dispatching a tool.

## How it works

A schema constrains shape. Application policy decides who may call a tool and on which resource. Bound the tool surface to a known registry, and route invalid requests to a reviewable outcome.

## Worked example

A reviewer may look up a team agenda. A guest with the same input shape has no permission, even when the tool is listed.

## Try it yourself

Run the allowed, denied, and invalid argument cases. Inspect where each decision is recorded.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Only a caller with the approved role and valid meeting ID reaches the tool.

## Continue

[← Previous lecture](01-discover-and-call-a-local-mcp-tool.md) · [Course outline](index.md) · [Next lecture →](03-persistent-approval-and-checkpoint-recovery.md)
