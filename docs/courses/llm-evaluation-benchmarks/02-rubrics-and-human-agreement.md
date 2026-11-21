# Rubrics and human agreement

<p class="study-position" data-course="llm-evaluation-benchmarks" data-lecture="02-rubrics-and-human-agreement.md">Design trustworthy evidence · Lecture 2 of 4</p>

[← Workload design and versioned cases](01-workload-design-and-versioned-cases.md) · [Course outline](index.md#course-outline){ .study-overview } · [Paired comparison across quality, cost and latency →](03-paired-comparison-across-quality-cost-and-latency.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design trustworthy evidence**

    - [Workload design and versioned cases](01-workload-design-and-versioned-cases.md)
    - **Rubrics and human agreement** (current)

    **Measure and decide**

    - [Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md)
    - [Release gates and selection memo](04-release-gates-and-selection-memo.md)

## What you will learn

Calibrate a binary rubric on paired reviewer labels before relying on an automated grader.

## An agreement figure needs disagreement examples

Two evaluators score one response differently because the evidence supports only half its claims. One judged the primary claim and the other judged every material claim.

Double-rate a shared sample and inspect the disagreement. Revise the rubric and report both raw and chance-adjusted agreement where meaningful. Then rerate a fresh subset to see whether the clarification worked.

## How it works

Write observable criteria. Report the confusion counts and both raw and chance-adjusted agreement for a binary grading task. Inspect disagreement cases and document adjudication. Perfect agreement with one label used everywhere may make chance adjustment undefined.

### Inspect what disagreement is telling you

A rubric should translate impressions into observable criteria. Review exact source support, completeness, and appropriate handoff separately. Two reviewers can agree on fluency while disagreeing on whether a major claim needs evidence. Make the consequential distinction explicit before collecting the final ratings.

Double-rate a subset and retain disagreement examples. Raw agreement is the fraction of matching ratings. A chance-adjusted measure asks how much agreement remains after accounting for the raters' overall use of each category. An imbalanced rubric can yield high raw agreement even when raters rarely agree on the rare failure.

Use the workbook to compare the measures, then read the underlying examples. If the wording caused different interpretations, update the rubric and rerate a fresh subset. If qualified reviewers still disagree, describe the uncertainty or escalate to a domain owner rather than creating a single spurious label.

## Worked example

Two reviewers agree on five of six assistant answers. The one disagreement involves a valid citation supporting only part of the claim.

## Try it yourself

Run the agreement calculation and inspect the disagreement. Rewrite one rubric criterion to resolve it.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A useful rewrite states that all material claims must be supported by the cited evidence and keeps abstention separate.

## Continue

[← Workload design and versioned cases](01-workload-design-and-versioned-cases.md) · [Course outline](index.md#course-outline){ .study-overview } · [Paired comparison across quality, cost and latency →](03-paired-comparison-across-quality-cost-and-latency.md)
{: .study-directions .study-directions--footer }
