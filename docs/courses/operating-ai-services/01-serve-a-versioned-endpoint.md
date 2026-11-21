# Serve a versioned endpoint

<p class="study-position" data-course="operating-ai-services" data-lecture="01-serve-a-versioned-endpoint.md">Package and observe · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Fallback, trace fields and durable telemetry →](02-fallback-trace-fields-and-durable-telemetry.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Package and observe**

    - **Serve a versioned endpoint** (current)
    - [Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md)

    **Release and recover**

    - [Canary evaluation and rollout decisions](03-canary-evaluation-and-rollout-decisions.md)
    - [Rollback and production handoff](04-rollback-and-production-handoff.md)

## What you will learn

Expose a local HTTP endpoint with explicit version and health behavior.

## Probe the route the caller will actually use

The service reports ready. A smoke request through the public interface gets the wrong version because routing wasn’t updated.

Probe readiness and the actual versioned response separately. Record caller-visible status and active version. It is possible for every component to be up and for the customer-facing route to be wrong.

## How it works

A model service has an externally testable contract and versioned implementation. Readiness answers whether the service may receive traffic. A smoke test sends a known request across the same transport the caller uses and checks the response and version.

### Probe the interface the caller uses

A deployable endpoint has a defined request shape, response shape, and behavior when an input is missing or a provider is unavailable. Include served version or another traceable revision, particularly when traffic is split. A health check answers whether a service can receive traffic. An end-to-end smoke request checks which behavior a real caller receives.

Separate process liveness from readiness. A process may be alive while the dependency needed to handle requests has not loaded. Conversely, a fallback could serve a reduced response even though the preferred route is temporarily unavailable. Choose a contract that makes this visible where it matters.

Use a known request in the workbook to verify both the route and its answer or handoff. Test invalid input as well. Capture the active version and actual result so later operators can tell whether traffic returned to the stable implementation.

## Worked example

A policy helper returns an answer or handoff plus the requested and served versions. A separate health endpoint lets routing detect an unavailable process.

## Try it yourself

Run the in-process application smoke check. Use the loopback HTTP smoke client in the final lecture to test the same contract through the network stack.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The response identifies the active version and health succeeds without invoking a model.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Fallback, trace fields and durable telemetry →](02-fallback-trace-fields-and-durable-telemetry.md)
{: .study-directions .study-directions--footer }
