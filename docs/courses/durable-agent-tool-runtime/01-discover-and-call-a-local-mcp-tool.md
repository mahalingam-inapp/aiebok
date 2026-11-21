# Discover and call a local MCP tool

<p class="study-position" data-course="durable-agent-tool-runtime" data-lecture="01-discover-and-call-a-local-mcp-tool.md">Connect and constrain · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Tool authorization and argument validation →](02-tool-authorization-and-argument-validation.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Connect and constrain**

    - **Discover and call a local MCP tool** (current)
    - [Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md)

    **Pause, recover and replay**

    - [Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md)
    - [Idempotent execution and decision traces](04-idempotent-execution-and-decision-traces.md)

## What you will learn

Trace the MCP initialization, tool discovery, and tool invocation over stdio.

## Read the tool declaration before treating it as a promise

The tool advertises an agenda lookup and a declared identifier field. It does not promise that the requester can see every agenda.

Inspect the declared input and validate the result against a known case. Discovery tells the client what exists. Application policy still determines which calls are permitted.

## How it works

A caller reaches a tool through a negotiated protocol and a declared input schema. With stdio transport, protocol messages use standard output and diagnostic messages use standard error. The notebook starts a minimal local fixture that offers a read-only agenda lookup.

### Discover a contract, then inspect it

An MCP client establishes a session with a compatible server and requests its tool definitions. A definition can describe the shape of inputs and the tool's purpose. It is useful evidence about how to form a request. The application must still decide whether a tool is appropriate and verify that its behavior meets that contract.

In the local exercise, use the agenda lookup in read-only mode and compare the listed schema with the actual result. Record the server version and one known output. When debugging, distinguish a transport error, an unknown operation, an invalid argument, and a successful call that returned no useful evidence.

Treat external tool descriptions as data from another boundary. A readable description does not give the server authority to change the caller’s task. Keep the allowed operations narrow, test permission separately, and make the failure state legible to the reviewer.

## Worked example

Initialize the session, discover lookup_agenda, and invoke it for a known meeting ID. Inspect the declared fields before sending arguments.

## Try it yourself

Run the discovery cell. Call lookup_agenda for the sample meeting and inspect the JSON-RPC result.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The server returns one typed tool declaration and a structured read result over the local process boundary.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Tool authorization and argument validation →](02-tool-authorization-and-argument-validation.md)
{: .study-directions .study-directions--footer }
