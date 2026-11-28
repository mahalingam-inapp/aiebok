# Constrain proposals and run checks

<p class="study-position" data-course="supervised-coding-harness" data-lecture="02-constrain-proposals-and-run-checks.md">Specify and verify a candidate · Lecture 2 of 4</p>

[← Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md) · [Course outline](index.md#course-outline){ .study-overview } · [Approval, revisions and replay →](03-approval-revisions-and-replay.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Specify and verify a candidate**

    - [Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md)
    - **Constrain proposals and run checks** (current)

    **Approve and audit a change**

    - [Approval, revisions and replay](03-approval-revisions-and-replay.md)
    - [Compare workflow traces and handoffs](04-compare-workflow-traces-and-handoffs.md)

## What you will learn

Validate the shape and scope of a proposed change before running the acceptance suite.

## A known proposal can still be wrong

A candidate uses a permitted operation but changes a part of the workflow outside the requested format. It passes a general style check.

Validate scope and run focused regression cases separately. Do not give an assistant arbitrary execution authority for a narrow formatting task. Give the reviewer the failing case and a small diff.

## How it works

A model can propose a typed change request without receiving a shell or arbitrary file-writing capability. In the workbook, a proposal selects one registered formatter. The harness rejects unknown actions and runs the same fixtures against each candidate. The review record retains test details.

### Check the proposal before granting effects

A harness can accept a small, typed proposal and run independent checks. Separate the declared operation and scope from the mechanism that applies it. An allowed field can still carry a change that violates the request, so validation of format and regression tests both matter.

A formatter proposal may name a recognized transformation and a known file. It can still change output for a legacy category outside the requested task. Evaluate the proposed behavior against the precise fixtures, and show the reviewer a diff small enough to inspect. A general lint pass adds evidence about style, which is weaker evidence about behavior.

Use a bounded sandbox or simulated effect for student exercises. Preserve the current state until a person has reviewed whatever needs approval. Record failures as evidence for the next attempt, such as a malformed proposal, an out-of-scope change, or a failing example. That makes review work measurable and prevents a retry from becoming blind expansion.

## Worked example

A known but incorrect formatter lowercases text while preserving doubled spaces. It passes some existing behaviors and still fails the added requirement.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from dataclasses import dataclass


def proposed_title(value):
    return " ".join(value.lower().split()) or "untitled"


CANDIDATES = {"current": current_title, "collapse-spaces": proposed_title}


@dataclass(frozen=True)
class Review:
    candidate: str
    revision: int
    failures: tuple
    approved: bool = False


def evaluate(proposal, revision):
    if (
        not isinstance(proposal, dict) or set(proposal) != {"action", "candidate"}
        or proposal["action"] != "update-formatter" or not isinstance(proposal["candidate"], str)
        or proposal["candidate"] not in CANDIDATES
    ):
        raise ValueError("proposal outside the allowed contract")
    candidate = proposal["candidate"]
    return Review(candidate, revision, tuple(regressions(CANDIDATES[candidate])))


proposal = {"action": "update-formatter", "candidate": "collapse-spaces"}
assert evaluate(proposal, 1).failures == ()
assert evaluate(proposal | {"candidate": "current"}, 1).failures
try:
    evaluate(proposal | {"action": "unregistered-action"}, 1)
except ValueError:
    pass
else:
    raise AssertionError("unknown action accepted")
```

## Try it yourself

Evaluate an unknown proposal and a known incorrect candidate. Compare the failure categories.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    An unknown proposal fails validation. A known candidate should return concrete test failures for the reviewer.

## Continue

[← Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md) · [Course outline](index.md#course-outline){ .study-overview } · [Approval, revisions and replay →](03-approval-revisions-and-replay.md)
{: .study-directions .study-directions--footer }
