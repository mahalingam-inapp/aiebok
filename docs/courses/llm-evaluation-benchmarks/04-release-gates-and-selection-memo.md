# Release gates and selection memo

<p class="study-position" data-course="llm-evaluation-benchmarks" data-lecture="04-release-gates-and-selection-memo.md">Measure and decide · Lecture 4 of 4</p>

[← Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Design trustworthy evidence**

    - [Workload design and versioned cases](01-workload-design-and-versioned-cases.md)
    - [Rubrics and human agreement](02-rubrics-and-human-agreement.md)

    **Measure and decide**

    - [Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md)
    - **Release gates and selection memo** (current)

## What you will learn

Apply hard quality thresholds before optimizing for cost or speed.

## Let the gate make ineligibility visible

The cheapest candidate fails a critical case and a better-scoring candidate misses the latency bound. The sponsor expects one winner.

Show each candidate’s blocked conditions and recommend only eligible options. If none qualify, record a hold and the test or mitigation that could change the decision.

## How it works

Set the gates before looking at results. Require enough evidence for critical slices, then compare eligible candidates by cost and latency. Save the reason, unresolved uncertainties, and what would reverse the decision.

### Keep a hold decision available

State the eligibility gates before comparing scores. A candidate may need to pass critical behaviors, have enough cases to support the estimate, and meet latency or cost limits. Rank only those that are eligible. This prevents a very large benefit on routine tasks from purchasing a smaller but unacceptable risk.

Describe the proposed release, conditions, and evidence together. An apparently strong candidate may need more samples on a language slice. Another may be acceptable for a read-only job but lack evidence for a more consequential action. Scope is part of the decision.

A decision memo should explain why a rejected option was held and what would change that result. Maintain the evaluation set and recorded version so a later rerun reflects a known change. If no option passes, retaining the current service is a legitimate outcome of the benchmark.

## Worked example

The lowest-cost candidate misses one access-boundary case. It is ineligible even if it wins aggregate cost.

## Try it yourself

Run the gated selection. Tighten the latency budget and see whether any candidate still qualifies.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A report can recommend holding all candidates. State the failed condition and choose what to investigate next.

## Continue

[← Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
