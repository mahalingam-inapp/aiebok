# Discovery and pilot acceptance

<p class="study-position" data-course="customer-pilot-engineering" data-lecture="01-discovery-and-pilot-acceptance.md">Discover and integrate · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Map a customer data contract →](02-map-a-customer-data-contract.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Discover and integrate**

    - **Discovery and pilot acceptance** (current)
    - [Map a customer data contract](02-map-a-customer-data-contract.md)

    **Evaluate and hand off**

    - [Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md)
    - [Rollout, operator handoff and stop rules](04-rollout-operator-handoff-and-stop-rules.md)

## What you will learn

Translate a request into a workflow, baseline, and measurable acceptance criteria.

## Translate vague enthusiasm into a measured goal

The sponsor asks for smart intake. The shift lead says reporters will still call if they cannot tell who owns a request.

Observe actual handoffs and name which delay the pilot must reduce. Establish manual median time, escalation behavior, and a safety gate. Ask the shift lead to confirm the expected human follow-up.

## How it works

Observe who does the work, what they decide, how long it takes, and who can approve a change. Separate a business outcome from service behavior. Define acceptance by case and agree on a comparison before building.

### Learn from the person doing the work

A pilot starts with a workflow and a customer decision. Watch how a real request moves through the current process, including the unofficial work people do to correct mistakes. Write the acceptance criterion in terms the shift lead can verify. Faster proposed routes are useful only if staff can recognize who owns the resulting ticket.

Use historical and synthetic cases to agree on what the pilot may touch. Establish the manual baseline, which work is sensitive, and when to ask a person. Decide which faults would pause the feature even if the average time improves. Protect an existing route for uncertain and restricted items.

Ask the customer to verify what an accepted result looks like using the evidence they normally work with. A successful demonstration is one repeatable observation, while acceptance also needs coverage and explicit ownership. Frame the smallest scope that can answer the customer’s real question.

## Worked example

A facilities manager asks for faster intake. Observe manual triage and target lower median time while preserving all restricted routing decisions.

## Try it yourself

Use the baseline time measurements in the workbook. Write a target and a guardrail that would both be observable during a pilot.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A defensible starting contract targets a 25% reduction in median time and requires every restricted case to be handed off.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Map a customer data contract →](02-map-a-customer-data-contract.md)
{: .study-directions .study-directions--footer }
