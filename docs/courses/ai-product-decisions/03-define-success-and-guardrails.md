# Define success and guardrails

<p class="study-position" data-course="ai-product-decisions" data-lecture="03-define-success-and-guardrails.md">Set evidence and limits · Lecture 3 of 4</p>

[← Compare rules, search, and generation](02-compare-rules-search-and-generation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Make a ship, revise, or stop decision →](04-make-a-ship-revise-or-stop-decision.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Find the right problem**

    - [Frame the decision before selecting a model](01-frame-the-decision-before-selecting-a-model.md)
    - [Compare rules, search, and generation](02-compare-rules-search-and-generation.md)

    **Set evidence and limits**

    - **Define success and guardrails** (current)
    - [Make a ship, revise, or stop decision](04-make-a-ship-revise-or-stop-decision.md)

## What you will learn

Write a primary metric and a separate quality threshold for a pilot.

## Measure the cases people would regret getting wrong

A pilot deflects more calls, but one caller reaches the wrong appointment queue because a preparation question was treated as a general one.

Keep deflection as a benefit metric. Add a separate gate for wrong routing on consequential cases and measure successful handoffs. Decide before launch which errors pause the trial.

## How it works

The primary metric describes the intended gain. A guardrail limits a downside that could make the gain unacceptable. Both need a population, a measurement method, and a decision threshold before the pilot begins.

### Pair benefits with a guardrail

A benefit measures the improvement you want, such as fewer repeat calls or less waiting. A guardrail measures a failure you cannot accept as the price of that improvement. Making them separate keeps good routine results from canceling out a consequential mistake.

Imagine the front desk redirects 60 of 100 routine callers to a useful source. The same pilot gives one incorrect instruction to a caller with a preparation question. Count the successful redirects, but report the consequential mistake in its own slice. A single combined number would hide which outcome the pilot is allowed to optimize.

Before release, name the denominator, acceptable limit, and person who reviews a breach. Give rejected or uncertain cases an explicit fallback. A stop rule should say what to pause and what continues. The front desk may keep serving the routine directory workload while preparation questions return to staff.

## Worked example

A routing pilot aims to cut median routing time by 20% while keeping the wrong-team rate at or below the current 5%. Measure on the same ticket categories under both methods.

### Follow the example

**Given:** The candidate routes 18 of 20 requests correctly. Its two failures are both urgent access requests.

**Walkthrough:** Keep urgent access requests on manual intake. Publish the urgent-case denominator alongside overall performance and set a separate gate for that group.

## Try it yourself

A draft assistant is supposed to save review time. Write one success criterion and one guardrail for customer notices.

??? success "Compare your answer"
    For example, reduce median total drafting and review time by 20% while allowing zero incorrect deadlines in the reviewed notices.

## Continue

[← Compare rules, search, and generation](02-compare-rules-search-and-generation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Make a ship, revise, or stop decision →](04-make-a-ship-revise-or-stop-decision.md)
{: .study-directions .study-directions--footer }
