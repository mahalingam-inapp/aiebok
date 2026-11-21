# Stage traces and failure localization

<p class="study-position" data-course="ai-reliability-release" data-lecture="02-stage-traces-and-failure-localization.md">Define and observe reliability · Lecture 2 of 4</p>

[← Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md) · [Course outline](index.md#course-outline){ .study-overview } · [Canary cohorts and staged gates →](03-canary-cohorts-and-staged-gates.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Define and observe reliability**

    - [Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md)
    - **Stage traces and failure localization** (current)

    **Release and recover**

    - [Canary cohorts and staged gates](03-canary-cohorts-and-staged-gates.md)
    - [Rollback verification and incident review](04-rollback-verification-and-incident-review.md)

## What you will learn

Use structured events to locate the earliest divergence between candidate and baseline.

## Start at the earliest stage that differs

Retrieval and validation look similar across versions. Generation in the pilot shows a long wait and failed calls.

Compare stage traces for stable and pilot requests with similar inputs. Separate observed divergence from the proposed cause. The operator needs a bounded reason to disable the candidate while deeper diagnosis continues.

## How it works

Record the first failing stage and bounded latency signals for retrieval, generation, and validation. Separate infrastructure failures from poor answer quality and group by version and cohort.

### Follow a trace from user outcome to the earliest divergence

A stage trace connects the user's result with what happened in routing, retrieval, generation, and validation. Record timings, versions, outcomes, and a request identity. Keep sensitive content out of telemetry when a category or identifier is enough. A low-level exception alone rarely tells an operator what the user experienced.

Compare an affected request with a similar stable one. Start at the earliest point where their behavior differs. Slow generation might be the visible issue, while the deeper cause could be an overly long context, a dependency delay, or a new route. Distinguish those observations from hypotheses.

Exercise the distinction in the lab by injecting a delay at a known stage. A report that attributes the failure correctly gives the next responder a bounded place to investigate. Include fallback behavior so served results do not hide a failed primary or an unexpected burden on staff.

## Worked example

Candidate users receive several timeouts during generation. Retrieval is fast for both cohorts, so the trace points investigation to the candidate dependency.

## Try it yourself

Run the failure aggregation and examine how the diagnosis changes if you move the injected failure to retrieval.

[Download the workbook](../../assets/notebooks/ai-reliability-release.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The dominant failing stage should follow the injection while stable traffic stays unaffected.

## Continue

[← Service objectives and error-budget burn](01-service-objectives-and-error-budget-burn.md) · [Course outline](index.md#course-outline){ .study-overview } · [Canary cohorts and staged gates →](03-canary-cohorts-and-staged-gates.md)
{: .study-directions .study-directions--footer }
