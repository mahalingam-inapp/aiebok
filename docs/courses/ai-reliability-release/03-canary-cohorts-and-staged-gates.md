# Canary cohorts and staged gates

<p class="study-position" data-course="ai-reliability-release" data-lecture="03-canary-cohorts-and-staged-gates.md">Release and recover · Lecture 3 of 4</p>

[← Stage traces and failure localization](02-stage-traces-and-failure-localization.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollback verification and incident review →](04-rollback-verification-and-incident-review.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Define and observe reliability**

    - [Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md)
    - [Stage traces and failure localization](02-stage-traces-and-failure-localization.md)

    **Release and recover**

    - **Canary cohorts and staged gates** (current)
    - [Rollback verification and incident review](04-rollback-verification-and-incident-review.md)

## What you will learn

Use predeclared coverage, burn, latency, and cost thresholds to approve or hold a rollout.

## Predeclare the stop rule for the small cohort

The whole-service error rate appears stable because most requests go to the baseline. The pilot has four failures among twenty requests.

Apply quality, latency, and cost gates to the pilot version with only its own denominator. Keep an explicit minimum sample and critical stop conditions. The aggregate cannot replace cohort evidence.

### Make the call while the stable version is available

Assume the release owner established a 95% threshold for on-time, valid responses and requires at least 20 candidate requests before deciding on expansion. The pilot records 16 good results in 20 attempts. That's 80% for the pilot. The baseline records 99 good results in 100 attempts. Combining both produces 115 good results in 120 attempts, or about 96%.

The combined number clears the threshold while the candidate fails it. Hold the candidate. Compare the earliest failed stage with comparable baseline requests and verify that the stable version can still serve the pilot users. A small cohort limits exposure. It does not make its missing or late work less important.

Now change the pilot to one failure in 20. The observed rate equals the threshold. Would you expand immediately? Check whether the minimum sample addresses the workload you are about to expose, including any consequential slice missing from the pilot.

## How it works

Keep stable and candidate traffic separately attributed and compare them over a defined window. A gate checks sample size, the critical failures, and cost before expanding. Report the exact gate that stops the rollout.

### Protect the canary from misleading averages

Assign a small cohort to the candidate and measure that cohort alongside comparable stable traffic. Record both the attempted and served versions, especially when fallback is enabled. If most requests use the baseline, a healthy aggregate can coexist with a candidate that fails much more often.

Predeclare a primary outcome, minimum observation requirement, and blocking conditions. Consider valid results, latency, fallback burden, and cost per usable task. Confirm that the canary contains the cases the release will serve. Missing evidence may justify holding the current exposure while collecting more data.

Keep the rollback route live and define who can invoke it. In the workbook, compare one passing and one failing cohort. An operator should be able to explain which criterion blocked expansion and what observation would justify resuming, without reverse-engineering the decision from a headline score.

## Worked example

A cheaper candidate misses the quality and latency gates during a 10% cohort. Pause that version and continue serving stable traffic.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def gate(rows, sample=20, burn_limit=2, latency_limit=350, cost_limit=0.003):
    if len(rows) < sample:
        return ["coverage"]
    info = objectives(rows)
    limits = (
        ("error_budget", info["burn"], burn_limit), ("latency", info["median_ms"], latency_limit),
        ("cost", info["mean_cost"], cost_limit),
    )
    return [name for name, observed, limit in limits if observed > limit]


assert gate(healthy) == []
assert gate(healthy[:1]) == ["coverage"]
assert gate(unhealthy) == ["error_budget"]
assert gate(unhealthy, burn_limit=21, cost_limit=0.001) == ["cost"]
```

## Try it yourself

Run a healthy and an unhealthy canary. Relax one gate and inspect which other condition still blocks promotion.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A canary passes only after all required evidence conditions pass. A low-cost result still needs adequate reliability.

## Continue

[← Stage traces and failure localization](02-stage-traces-and-failure-localization.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollback verification and incident review →](04-rollback-verification-and-incident-review.md)
{: .study-directions .study-directions--footer }
