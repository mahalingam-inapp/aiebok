# Discover and call a local MCP tool

[Durable Agent Runtime and MCP](index.md) · Connect and constrain · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Trace the MCP initialization, tool discovery, and tool invocation over stdio.

## How it works

A caller reaches a tool through a negotiated protocol and a declared input schema. With stdio transport, protocol messages use standard output and diagnostic messages use standard error. The notebook starts a minimal local fixture that offers a read-only agenda lookup.

## Worked example

Initialize the session, discover lookup_agenda, and invoke it for a known meeting ID. Inspect the declared fields before sending arguments.

## Try it yourself

Run the discovery cell. Call lookup_agenda for the sample meeting and inspect the JSON-RPC result.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The server returns one typed tool declaration and a structured read result over the local process boundary.

## Continue

[Course outline](index.md) · [Next lecture →](02-tool-authorization-and-argument-validation.md)
