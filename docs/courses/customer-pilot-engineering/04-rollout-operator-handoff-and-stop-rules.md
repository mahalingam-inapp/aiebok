# Rollout, operator handoff and stop rules

<p class="study-position" data-course="customer-pilot-engineering" data-lecture="04-rollout-operator-handoff-and-stop-rules.md">Evaluate and hand off · Lecture 4 of 4</p>

[← Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Discover and integrate**

    - [Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md)
    - [Map a customer data contract](02-map-a-customer-data-contract.md)

    **Evaluate and hand off**

    - [Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md)
    - **Rollout, operator handoff and stop rules** (current)

## What you will learn

Write a release recommendation grounded in measured outcomes and assign an operational owner.

## Hand over a decision someone can operate

The pilot reaches its time target on routine tickets. The shift lead worries about what happens when someone submits a restricted request tomorrow.

Show the restricted-case result and a working stop rule. Name the owner of manual fallback, provide a reproducible smoke case, and document how the customer can pause the pilot without the engineering team.

## How it works

Report the cohort, case counts, observed limitations, and actions after launch. A stop rule links evidence to an action and owner. The handoff includes a smoke case, fallback route, data boundary, and how to read the service record.

### The pilot is only as reversible as the handoff

A customer-facing release needs a named owner, a defined scope, a known smoke case, and an accessible fallback. Report which tasks passed and which still go to staff. Include the threshold that triggers pause and explain how to identify requests handled during the pilot.

Give the shift lead a small rehearsal. Have them recognize a failure, pause the feature, find an in-flight item, and confirm it remains in the manual queue. The ability to follow a runbook becomes part of acceptance evidence. A handoff is incomplete if preserving the workflow still requires the developer to be present.

Keep a log of responsibilities and a checkpoint for reassessment. A bounded approval can be extended later when the customer has enough evidence on new categories. A limited release that the operators can understand and reverse is often more valuable than a broader demonstration with uncertain ownership.

## Worked example

The pilot meets its median time target, but a restricted case routes automatically. The owner keeps manual triage active and blocks expansion.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def decide(observed_times, restricted_case_ok, completed_smoke_test):
    return (
        len(observed_times) >= len(baseline_minutes)
        and median(observed_times) <= median_target
        and restricted_case_ok
        and completed_smoke_test
    )


pilot_minutes = (6, 7, 8, 9, 11)
assert decide(pilot_minutes, True, True)
assert not decide(pilot_minutes, False, True)
assert not decide(pilot_minutes[:2], True, True)
print({
    "pilot_cohort": "simulated facilities intake",
    "cases": len(pilot_minutes),
    "median_minutes": median(pilot_minutes),
    "recommendation": "bounded pilot",
    "operator_owner": "facilities shift lead",
    "stop_rule": "route any restricted case manually and pause automation",
    "smoke_case": {"input_id": "F2", "expected": "review"},
})
```

## Try it yourself

Review both bundled pilot result sets. Write a one-page handoff with the same triggers.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Recommend controlled adoption only when the thresholds pass. Identify who can pause the service and how affected work is handled.

## Continue

[← Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
