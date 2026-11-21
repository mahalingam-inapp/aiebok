# Fallback, trace fields and durable telemetry

<p class="study-position" data-course="operating-ai-services" data-lecture="02-fallback-trace-fields-and-durable-telemetry.md">Package and observe · Lecture 2 of 4</p>

[← Serve a versioned endpoint](01-serve-a-versioned-endpoint.md) · [Course outline](index.md#course-outline){ .study-overview } · [Canary evaluation and rollout decisions →](03-canary-evaluation-and-rollout-decisions.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Package and observe**

    - [Serve a versioned endpoint](01-serve-a-versioned-endpoint.md)
    - **Fallback, trace fields and durable telemetry** (current)

    **Release and recover**

    - [Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md)
    - [Rollback and production handoff](04-rollback-and-production-handoff.md)

## What you will learn

Record provider failures and successful fallback without storing request text.

## Tell the operator what the fallback did

The fallback returns a result, but Helena sees only a successful transport status. The primary is still failing and work handed to staff is piling up.

Record requested and served versions, elapsed time, and fallback reason without storing sensitive input. Query failures by requested version so a successful fallback doesn’t hide a broken candidate.

## How it works

A fallback may preserve availability while hiding primary failures from aggregate success. Measure the primary failure rate separately. Capture request ID, requested and served versions, elapsed time, and the fallback outcome. Persist the telemetry so the release gate can query it.

### Give fallback behavior its own operational record

When a primary route fails, fallback can maintain a useful outcome. It can also hide reliability problems if the dashboard counts every response the same way. A successful handoff might still consume staff time. Record what was requested, what actually served, and why those choices differed.

A structured trace can include a request identifier, attempted version, served version, status, elapsed time, and fallback reason. Avoid storing personal request text where counts and identifiers suffice. Choose retention and access deliberately so support can investigate an incident without making routine observability a new source of exposure.

Persist the events needed for release evaluation. A worker restart should not erase the recent evidence for a failing canary. Run one forced timeout and query the resulting record. If the public response was correct and the events still show a primary failure, the telemetry is describing the system that operators need to run.

## Worked example

A candidate fails to answer during a dry run. The baseline serves it and the trace preserves the fact that a fallback occurred.

## Try it yourself

Trigger the bundled provider failure. Query the telemetry and check that sensitive request text is absent.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The stored row should show the candidate as requested and baseline as served with a fallback flag.

## Continue

[← Serve a versioned endpoint](01-serve-a-versioned-endpoint.md) · [Course outline](index.md#course-outline){ .study-overview } · [Canary evaluation and rollout decisions →](03-canary-evaluation-and-rollout-decisions.md)
{: .study-directions .study-directions--footer }
