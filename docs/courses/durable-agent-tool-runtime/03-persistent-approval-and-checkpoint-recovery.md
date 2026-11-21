# Persistent approval and checkpoint recovery

<p class="study-position" data-course="durable-agent-tool-runtime" data-lecture="03-persistent-approval-and-checkpoint-recovery.md">Pause, recover and replay · Lecture 3 of 4</p>

[← Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Idempotent execution and decision traces →](04-idempotent-execution-and-decision-traces.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Connect and constrain**

    - [Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md)
    - [Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md)

    **Pause, recover and replay**

    - **Persistent approval and checkpoint recovery** (current)
    - [Idempotent execution and decision traces](04-idempotent-execution-and-decision-traces.md)

## What you will learn

Persist a proposal and its approval against a payload fingerprint, then reopen the runtime.

## Persist what the reviewer actually saw

Jo approves a draft after the workflow restarts. A corrected draft exists with a different payload.

Persist the proposed payload and its fingerprint before pause. Bind the human decision to exactly that version. A changed payload should be reviewed anew.

## How it works

Persist pending work before waiting for a reviewer. Bind approval to the specific proposal so a modified payload needs review. On restart, reconstruct the next permitted transition from stored state.

### Persist the state a person saw when they approved

A waiting workflow needs data that can survive restart: the proposed effect, its exact revision, who can approve it, the recorded approval state, and the next legal transition. If the worker only holds that state in memory, a restart can transform an approved or pending effect into an ambiguous one.

Bind approval to the reviewed version. In the agenda exercise, change the note after storing a pending request and verify that approval for the old note cannot apply to the revision. Restore a checkpoint in a fresh process and confirm it reports whether the workflow is still waiting.

Approval and completion are distinct facts. An approval authorizes an effect under specified conditions. A completion record reports that the effect happened. If an operation can succeed while a response is lost, retain a stable identifier and a reconciliation route. Resume only after you can tell which facts are already durable.

## Worked example

A reviewer approves a note for meeting M1. Editing the text after review changes its fingerprint, so the previous approval no longer applies.

## Try it yourself

Reopen the SQLite store after creating a proposal. Verify that pending work stays pending and compare a mismatched approval.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The record survives a restart and the wrong fingerprint leaves it awaiting approval.

## Continue

[← Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Idempotent execution and decision traces →](04-idempotent-execution-and-decision-traces.md)
{: .study-directions .study-directions--footer }
