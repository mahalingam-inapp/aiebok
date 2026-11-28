# Service objectives and error-budget burn

<p class="study-position" data-course="ai-reliability-release" data-lecture="01-service-objectives-and-error-budget-burn.md">Define and observe reliability · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Stage traces and failure localization →](02-stage-traces-and-failure-localization.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Define and observe reliability**

    - **Service objectives and error-budget burn** (current)
    - [Stage traces and failure localization](02-stage-traces-and-failure-localization.md)

    **Release and recover**

    - [Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md)
    - [Rollback verification and incident review](04-rollback-verification-and-incident-review.md)

## What you will learn

Define a good request and calculate reliability and budget burn over a bounded window.

## A user can receive a response and still lose time

A late summary eventually arrives, after an agent already opened a second ticket to work around the delay. Transport success stays green.

Define a good outcome in terms of valid and timely work. Use the cohort denominator and the agreed objective to estimate burn. Keep the observation window and sample size attached to the number.

## How it works

A service objective uses outcomes a user cares about, such as a valid, grounded result delivered under a latency bound. The error budget is the allowed fraction of bad requests. Burn rate compares the observed bad fraction with that allowance.

### Count a good request as the caller experiences it

A service-level indicator should define a usable result. For an assistant, that could require a valid answer or useful handoff within a deadline. A transport success with a late, malformed, or unsupported result might fail this definition. State the eligible population and observation window.

An objective of 99% good results allows 1% bad results in the chosen window. If the measured bad rate is 5%, the budget is being consumed at five times the allowed rate for that window. Burn expresses the pace of failure relative to the target, rather than the total incident impact on its own.

Check the cohort denominator and sample size. A small sample can be enough to reveal a severe problem, even though it gives a noisy estimate of the true rate. Decide when to alert, when to gather more evidence, and when a critical failure independently requires pausing.

## Worked example

With a 99% objective, a 5% bad rate burns error budget at five times the sustainable rate.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from dataclasses import dataclass
from statistics import median


@dataclass(frozen=True)
class Trace:
    cohort: str
    version: str
    stages_ms: tuple[tuple[str, int], ...]
    valid: bool
    failed_at: str | None = None
    cost: float = 0.002

    @property
    def elapsed(self):
        return sum(value for _, value in self.stages_ms)


def trace(cohort, version, bad=False):
    return Trace(cohort, version, (("retrieval", 20), ("generation", 900 if bad else 180), ("validation", 15)),
                 not bad, "generation" if bad else None)


stable = [trace("control", "v1") for _ in range(20)]
healthy = [trace("pilot", "v2") for _ in range(20)]
unhealthy = [trace("pilot", "v2", bad=i < 4) for i in range(20)]


def objectives(rows, latency_limit=350, target=0.99):
    good = sum(row.valid and row.elapsed <= latency_limit for row in rows)
    bad_fraction = (len(rows) - good) / len(rows)
    return {"n": len(rows), "good": good, "burn": bad_fraction / (1 - target),
            "median_ms": median(row.elapsed for row in rows), "mean_cost": sum(row.cost for row in rows) / len(rows)}


assert objectives(stable)["burn"] == 0
assert abs(objectives(unhealthy)["burn"] - 20) < 1e-8
```

## Try it yourself

Compute objectives for the fixture cohorts. Change the latency threshold and decide which failures count.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A successful transport can still be a bad outcome if the result is invalid or late. State the denominator and report low sample counts.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Stage traces and failure localization →](02-stage-traces-and-failure-localization.md)
{: .study-directions .study-directions--footer }
