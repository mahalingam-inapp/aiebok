# Agent Runtime and MCP Engineer Capstone

Build a supervised local workflow to review and record a meeting agenda note. Extend the [Durable Agent Runtime and MCP lab](../../courses/durable-agent-tool-runtime/index.md) with a second read-only tool or a second synthetic meeting.

## Milestones

1. Capture an initialization, discovery, and permitted tool-call transcript. Show one rejected call and document where caller policy is enforced.
2. Persist a proposed effect and an approval scoped to the exact payload. Restart before approval and verify that work still waits.
3. Resume and replay after completion. Demonstrate one durable effect and explain how the design would change if the effect were sent to a remote service.

## Rubric

| Evidence | Complete when |
|---|---|
| Tool boundary | The schema is inspectable and inappropriate input or role is rejected before dispatch. |
| Checkpoint and approval | Reopened state retains the pending proposal and rejects stale approval. |
| Recovery | A completion replay returns a recorded outcome, with one local effect and a clear explanation of remote failure handling. |

[Back to the learning path](agent-runtime-mcp-engineer.md)
