# Canary evaluation and rollout decisions

<p class="study-position" data-course="operating-ai-services" data-lecture="03-canary-evaluation-and-rollout-decisions.md">Release and recover · Lecture 3 of 4</p>

[← Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollback and production handoff →](04-rollback-and-production-handoff.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Package and observe**

    - [Serve a versioned endpoint](01-serve-a-versioned-endpoint.md)
    - [Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md)

    **Release and recover**

    - **Canary evaluation and rollout decisions** (current)
    - [Rollback and production handoff](04-rollback-and-production-handoff.md)

## What you will learn

Compare gated evidence and identify a canary that must pause.

## Hold the canary even if the aggregate is green

Stable requests dominate traffic. The candidate exceeds its fallback rate for one cohort, but overall success still looks good.

Apply the gate to the candidate cohort with a predeclared denominator. Require enough observations and a tolerable operational burden. Record why you held rollout and the evidence needed to retry.

## How it works

A canary is a limited rollout of a labeled version. Define sample requirements, acceptable fallback or error rates, and a latency bound. Evaluate on traffic attributed to the requested version, so fallbacks do not improve the apparent reliability of the failing version.

### Evaluate the candidate cohort on its own merits

A canary limits the group receiving a proposed version. The gate must still examine the candidate group separately. Stable traffic can dominate the aggregate and obscure a regression in a small trial. Record how cases are assigned and which version the request attempted to use.

Choose a minimum useful observation count and high-priority criteria before looking at results. Check latency, fallback reason, and valid user outcome. An aggregate availability signal is useful for alerting, but insufficient for deciding whether a version should receive additional traffic. Compare like workloads so a batch of unusually easy requests does not accidentally justify expansion.

If the candidate fails, preserve both the decision and evidence. Decide whether to hold at the current scope, disable it, or investigate a confounding factor. A good release tool distinguishes “failed the gate” from “insufficient evidence” so operators know whether to change the system or gather more observations.

## Worked example

If the candidate has two failures in ten comparable requests and the maximum is one in ten, pause even when all ten callers received some response.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def gate(store, version, minimum=4, max_fallback_rate=0.2, p95_limit_ms=1000):
    rows = store.conn.execute(
        "SELECT elapsed_ms, fallback FROM traces WHERE requested = ? ORDER BY elapsed_ms", (version,)
    ).fetchall()
    if len(rows) < minimum:
        return False, f"insufficient sample ({len(rows)}/{minimum})"
    rate = sum(fallback for _, fallback in rows) / len(rows)
    from math import ceil
    p95 = rows[ceil(0.95 * len(rows)) - 1][0]
    return rate <= max_fallback_rate and p95 <= p95_limit_ms, f"fallback rate {rate:.1%}, p95 {p95:.2f} ms"


assert gate(store, "v2")[1].startswith("insufficient sample")
for question in ("special request", "reserve a room", "reserve a room"):
    request(service, "/predict", {"question": question}, canary=True)
passed, reason = gate(store, "v2")
assert not passed and "50.0%" in reason
for _ in range(3):
    request(service, "/predict", {"question": "reserve a room"})
assert gate(store, "v1")[0]
print("Canary", reason)
```

## Try it yourself

Run the gate with a limited candidate cohort and compare its decision with normal traffic. The notebook uses a loopback request header to select the fixture cohort. In a deployed service, assign cohorts in trusted routing infrastructure.

[Download the workbook](../../assets/notebooks/operating-ai-services.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    An insufficient sample should fail with a coverage reason. A well-sampled unhealthy candidate should fail with the measured rate.

## Continue

[← Fallback, trace fields and durable telemetry](02-fallback-trace-fields-and-durable-telemetry.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollback and production handoff →](04-rollback-and-production-handoff.md)
{: .study-directions .study-directions--footer }
