# Idempotent execution and decision traces

<p class="study-position" data-course="durable-agent-tool-runtime" data-lecture="04-idempotent-execution-and-decision-traces.md">Pause, recover and replay · Lecture 4 of 4</p>

[← Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Connect and constrain**

    - [Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md)
    - [Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md)

    **Pause, recover and replay**

    - [Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md)
    - **Idempotent execution and decision traces** (current)

## What you will learn

Commit a local effect exactly once across retries and distinguish external effects.

## A replay is neither a new note nor a new approval

A write completes and the worker is interrupted before the caller sees success. On restart, the same command arrives.

Commit the local note and its completion record atomically. Use the command identity to return the existing result on replay. For external effects, rely on the external idempotency contract or reconcile before trying again.

## How it works

Record the action and its state transition in the same transaction for a local database effect. A retry can then find the completed record. A remote effect needs its own idempotency contract or a reconciliation process.

### Define what a replay is allowed to do

An idempotent operation can accept repeated requests for the same intended effect without producing a second effect. Use a stable identity tied to the logical operation, not a new identifier for each delivery attempt. With a local database, committing a note and its completion record together gives the next worker one place to inspect.

A remote service may complete a write before the caller times out. Local memory alone cannot tell whether it happened. Use the service's idempotency contract where possible, otherwise reconcile before retrying. When evidence still cannot establish what happened, stop and ask an operator instead of sending a second notification blindly.

Log the operation identity, reviewed revision, effect state, and retry disposition. Verify a successful repeat returns the prior result and a genuinely changed request needs a new decision. The trace should explain why the system resumed, waited, or declined to repeat the action.

## Worked example

The worker restarts after saving an approved agenda note and before returning success. The next attempt reports the existing completion.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def execute(db, identifier):
    with db:
        db.execute("BEGIN IMMEDIATE")
        row = db.execute("SELECT payload, approved FROM proposals WHERE id = ?", (identifier,)).fetchone()
        if row is None or not row[1]:
            return "awaiting_approval"
        effect = db.execute("INSERT OR IGNORE INTO notes VALUES (?, ?)", (identifier, row[0]))
        return "completed" if effect.rowcount else "replayed"


assert execute(db, "proposal-1") == "awaiting_approval"
assert approve(db, "proposal-1", digest)
assert execute(db, "proposal-1") == "completed"
db.close()
db = open_store(database)
try:
    assert execute(db, "proposal-1") == "replayed"
    assert db.execute("SELECT count(*) FROM notes").fetchone() == (1,)
    print("Decision trace", events + ["awaiting_approval", "approved", "completed", "replayed"])
finally:
    db.close()
    directory.cleanup()
```

## Try it yourself

Reopen the store again and replay the approved action. Check the persistent effect count and trace.

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The replay reports the existing result and there is one note. Explain why this guarantee would change for a remote calendar API.

## Continue

[← Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
