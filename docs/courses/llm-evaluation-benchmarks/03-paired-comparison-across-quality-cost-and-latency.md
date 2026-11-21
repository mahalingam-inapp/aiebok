# Paired comparison across quality, cost and latency

<p class="study-position" data-course="llm-evaluation-benchmarks" data-lecture="03-paired-comparison-across-quality-cost-and-latency.md">Measure and decide · Lecture 3 of 4</p>

[← Rubrics and human agreement](02-rubrics-and-human-agreement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Release gates and selection memo →](04-release-gates-and-selection-memo.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design trustworthy evidence**

    - [Workload design and versioned cases](01-workload-design-and-versioned-cases.md)
    - [Rubrics and human agreement](02-rubrics-and-human-agreement.md)

    **Measure and decide**

    - **Paired comparison across quality, cost and latency** (current)
    - [Release gates and selection memo](04-release-gates-and-selection-memo.md)

## What you will learn

Report per-slice quality, a paired uncertainty interval, latency, and cost per correct task.

## Compare successes and the cost of failures

The fast candidate is cheap per request but produces more outputs requiring review. A careful candidate is slow and handles some difficult cases better.

Use paired quality differences on the same workload and include the uncertainty associated with a small sample. Compare latency and cost per correct task, including paid failures and clearly identified review assumptions.

## How it works

Evaluate candidates on identical cases and resample paired score differences to preserve that comparison. Keep sample size visible and explain why a tiny set has wide uncertainty. Cost per correct task includes spend on failures. Report unavailable metrics explicitly.

### Pair cases before comparing candidates

When candidates see the same tasks, compare the results case by case. An improvement on one case and a regression on another can cancel in the mean. The paired record lets a reviewer find that trade. Repeatedly sampling paired observations can provide an interval for the observed difference, within the assumptions of the sample.

Report latency with attempts and timeouts. Include all paid requests in cost per correct task. A candidate charging a small amount per call can be expensive per accepted result if it often requires retries or human correction. State what your cost estimate includes and what it leaves out.

Inspect critical slices before ranking the full sample. Report counts and assess how representative they are. A lower-cost candidate with one additional consequential failure may be ineligible even when its average quality estimate is comparable. The decision depends on the separate gate agreed before evaluation.

## Worked example

A cheap model can cost more per correct result when its mistakes are frequent. A higher median score can coexist with a critical-slice regression.

## Try it yourself

Run the three fixture candidates and compare the paired delta. Recompute after changing the seed or sample mix.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Interpret the interval as uncertainty for this workload and investigate any weak critical slice before recommending a candidate.

## Continue

[← Rubrics and human agreement](02-rubrics-and-human-agreement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Release gates and selection memo →](04-release-gates-and-selection-memo.md)
{: .study-directions .study-directions--footer }
