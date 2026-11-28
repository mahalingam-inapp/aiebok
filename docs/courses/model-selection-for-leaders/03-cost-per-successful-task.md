# Cost per successful task

<p class="study-position" data-course="model-selection-for-leaders" data-lecture="03-cost-per-successful-task.md">Compare economics and decide · Lecture 3 of 4</p>

[← Interpret quality evidence and uncertainty](02-interpret-quality-evidence-and-uncertainty.md) · [Course outline](index.md#course-outline){ .study-overview } · [Make a bounded selection decision →](04-make-a-bounded-selection-decision.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Frame the decision**

    - [Specify the workload and critical failures](01-specify-the-workload-and-critical-failures.md)
    - [Interpret quality evidence and uncertainty](02-interpret-quality-evidence-and-uncertainty.md)

    **Compare economics and decide**

    - **Cost per successful task** (current)
    - [Make a bounded selection decision](04-make-a-bounded-selection-decision.md)

## What you will learn

Calculate cost per correct result and include review effort in the decision.

## Count the cost of an answer that still needs fixing

A candidate costs 12 units for a run and gives 9 acceptable answers. A second costs 20 units and also gives 9, but its reviewers spend less time correcting outputs.

The measured service costs are about 1.33 and 2.22 per acceptable answer. Compare them after adding reviewer time at a consistent rate. Keep costs and critical failure gates separate.

## How it works

Divide total spend on the cases by the number of correct outcomes. Review and rework contribute to operating costs. Report latency and reliability on the actual workflow because they change who can use the system.

### Price useful work

A cost per call can look low while a cost per completed task is high. Include retries, reviews, corrections, and any paid requests that failed. If a service costs 12 units to attempt 10 tasks and 9 meet the agreed checks, its observed cost per correct result is about 1.33 units before review.

Time is another part of the cost. Two candidates with the same total bill may differ in reviewer effort and the delay they impose on staff. If one needs five extra minutes per case or more rounds of clarification, an inexpensive inference bill can be misleading.

Use a consistent workload and report the limits of the comparison. Price estimates at modest volume may miss peaks, implementation effort, or support. Separate known costs from assumptions. This makes it easier to recalculate the recommendation if the volume, reviewer rate, or vendor terms change.

## Worked example

Balanced costs 0.026 units for nine correct cases. Careful costs 0.051 units for ten correct cases.

### Follow the example

**Given:** A low-cost endpoint needs twice as many manual checks as its competitor.

**Walkthrough:** Combine price, verified successes, and reviewer minutes. Include escalation staffing and the cost of retreating to the current process.

## Try it yourself

Compare cost per correct result for both candidates, then identify one expense the benchmark omits.

??? success "Compare your answer"
    Balanced costs about 0.0029 per correct result and Careful costs 0.0051. Human review time is a separate line item.

## Continue

[← Interpret quality evidence and uncertainty](02-interpret-quality-evidence-and-uncertainty.md) · [Course outline](index.md#course-outline){ .study-overview } · [Make a bounded selection decision →](04-make-a-bounded-selection-decision.md)
{: .study-directions .study-directions--footer }
