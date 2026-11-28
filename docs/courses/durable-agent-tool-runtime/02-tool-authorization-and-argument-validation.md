# Tool authorization and argument validation

<p class="study-position" data-course="durable-agent-tool-runtime" data-lecture="02-tool-authorization-and-argument-validation.md">Connect and constrain · Lecture 2 of 4</p>

[← Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md) · [Course outline](index.md#course-outline){ .study-overview } · [Persistent approval and checkpoint recovery →](03-persistent-approval-and-checkpoint-recovery.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Connect and constrain**

    - [Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md)
    - **Tool authorization and argument validation** (current)

    **Pause, recover and replay**

    - [Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md)
    - [Idempotent execution and decision traces](04-idempotent-execution-and-decision-traces.md)

## What you will learn

Validate caller scope and arguments before dispatching a tool.

## The same valid payload can be unauthorized

A reviewer and a guest supply the same meeting identifier. Both requests satisfy the input schema.

Check caller and resource policy in addition to argument shape. Record a denied request without sending it to the tool. This keeps a correctness check from being mistaken for authorization.

## How it works

A schema constrains shape. Application policy decides who may call a tool and on which resource. Bound the tool surface to a known registry, and route invalid requests to a reviewable outcome.

### Check both the argument and the actor

Validation asks whether a request has a well-formed resource identifier and expected fields. Authorization asks whether this caller can perform that operation for that resource. A guest and an approved reviewer can send identical valid payloads and should receive different outcomes.

Perform the authorization check in the trusted application or service boundary before dispatch. Use the caller identity provided by that boundary rather than a role asserted by generated text. Give read-only operations and persistent writes separate decisions. On a denial, return a controlled outcome with enough context for an operator to investigate.

Write paired tests for the same resource and different roles, plus a malformed request from an allowed role. The malformed case proves shape is checked. The paired case proves shape does not substitute for authority. Record the rejected reason without logging more request data than necessary.

## Worked example

A reviewer may look up a team agenda. A guest with the same input shape has no permission, even when the tool is listed.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
events = []


def lookup(role, meeting):
    if role != "reviewer":
        events.append("denied")
        return None
    if meeting != "M1":
        events.append("invalid_arguments")
        return None
    result = exchange("tools/call", {"name": "lookup_agenda", "arguments": {"meeting": meeting}})
    events.append("read")
    return result["content"][0]["text"]


assert lookup("guest", "M1") is None
assert lookup("reviewer", "M9") is None
assert lookup("reviewer", "M1") == "Review the accessibility checklist."
assert events == ["denied", "invalid_arguments", "read"]
```

## Try it yourself

Run the allowed, denied, and invalid argument cases. Inspect where each decision is recorded.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Only a caller with the approved role and valid meeting ID reaches the tool.

## Continue

[← Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md) · [Course outline](index.md#course-outline){ .study-overview } · [Persistent approval and checkpoint recovery →](03-persistent-approval-and-checkpoint-recovery.md)
{: .study-directions .study-directions--footer }
