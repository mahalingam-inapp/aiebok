# Rollback and production handoff

<p class="study-position" data-course="operating-ai-services" data-lecture="04-rollback-and-production-handoff.md">Release and recover · Lecture 4 of 4</p>

[← Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Package and observe**

    - [Serve a versioned endpoint](01-serve-a-versioned-endpoint.md)
    - [Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md)

    **Release and recover**

    - [Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md)
    - **Rollback and production handoff** (current)

## What you will learn

Persist a version-pointer rollback and verify it through a local HTTP smoke test.

## Recovery is a new observation

The on-call operator moves the active pointer back to the last stable revision. Staff still need confirmation that new requests use the intended version.

Reopen the state if relevant and send a smoke request through the serving interface. Compare requested and served versions and log the decision. A successful configuration write is not itself evidence of recovery.

## How it works

Rollback restores the previous serving version. Keep the decision durable and include it in the operator log. After changing the pointer, send a smoke request through the serving endpoint. In hosted environments, use a managed secret store, readiness checks, and an explicit release owner.

### Verify the service after restoring the pointer

Rollback is a new deployment decision. Use the prior known-good version, record who authorized it and why, then verify the observed route. A successful configuration write can coexist with stale workers, cached policy, or new requests still being routed to the candidate.

Run a smoke check from the perspective of both a stable caller and a caller affected by the candidate. Check the served version, result, and health of any manual queue that received fallback work. If the candidate caused inconsistent or pending effects, decide how operators will reconcile those separately.

Persist the pointer and event history if service continuity depends on surviving restart. Reopen the store in the workbook and repeat the request. The handoff should tell a colleague what failed, which version is safe to use, what remains pending, and which evidence would permit the next release.

## Worked example

A blocked canary reassigns the production pointer to v1. After reopening its state store, the next request reports v1 and the decision log still contains the rollback.

## Try it yourself

Run rollback, reopen the store, and make a loopback HTTP health and prediction request. Write your runbook with the measurable trigger and post-rollback check.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The version pointer and decision survive reopen. The deployed service reports its baseline version through HTTP.

## Continue

[← Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
