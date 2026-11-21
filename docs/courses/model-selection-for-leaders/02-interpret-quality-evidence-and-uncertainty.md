# Interpret quality evidence and uncertainty

<p class="study-position" data-course="model-selection-for-leaders" data-lecture="02-interpret-quality-evidence-and-uncertainty.md">Frame the decision · Lecture 2 of 4</p>

[← Specify the workload and critical failures](01-specify-the-workload-and-critical-failures.md) · [Course outline](index.md#course-outline){ .study-overview } · [Cost per successful task →](03-cost-per-successful-task.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Frame the decision**

    - [Specify the workload and critical failures](01-specify-the-workload-and-critical-failures.md)
    - **Interpret quality evidence and uncertainty** (current)

    **Compare economics and decide**

    - [Cost per successful task](03-cost-per-successful-task.md)
    - [Make a bounded selection decision](04-make-a-bounded-selection-decision.md)

## What you will learn

Read aggregate and critical-slice scores without hiding the size of the test.

## A perfect tiny sample is provisional

Two testers agree that one candidate passed both critical checks. Its sales lead claims a perfect critical accuracy rate for future traffic.

Record the denominator and scope. Two pass cases are evidence about those two inputs. Ask for more cases from the actual workload and for examples where graders initially disagreed.

## How it works

A score without a denominator says little about uncertainty. Ask whether the examples represent the workload and whether reviewers agreed on grading. Track critical failures independently.

### Read denominators before reading rankings

Nine successes in ten attempts and 90 in 100 share a percentage. They do not offer the same confidence about what happens next. Keep the count, type of cases, and any exclusions attached to the score. Look at errors that matter separately from errors a staff member can quickly correct.

Several reviewers can also disagree about what counts as support. Ask them to rate a common subset and record where they differ. Inspect cases where a major claim relied on a weak source or where an apparently incomplete response was actually a correct handoff. Agree on the rule before using it to compare candidates.

For a purchase, ask for the workload that the trial did not cover. A model may have passed all tested examples and still have no evidence on the regional languages or exception types that your users need. Keep untested work out of approved scope or plan how to get the missing evidence.

## Worked example

Fast and Balanced each pass 9 of 10 fixture cases. Fast misses one of two important cases, so the same overall score conceals a different risk.

## Try it yourself

Identify which score prevents Fast from being eligible and why the test is still limited.

??? success "Compare your answer"
    Fast misses the critical gate. Ten cases can justify a limited trial with further evidence, and other traffic may behave differently.

## Continue

[← Specify the workload and critical failures](01-specify-the-workload-and-critical-failures.md) · [Course outline](index.md#course-outline){ .study-overview } · [Cost per successful task →](03-cost-per-successful-task.md)
{: .study-directions .study-directions--footer }
