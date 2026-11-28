# Write an acceptance contract for a change

<p class="study-position" data-course="supervised-coding-harness" data-lecture="01-write-an-acceptance-contract-for-a-change.md">Specify and verify a candidate · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Constrain proposals and run checks →](02-constrain-proposals-and-run-checks.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Specify and verify a candidate**

    - **Write an acceptance contract for a change** (current)
    - [Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md)

    **Approve and audit a change**

    - [Approval, revisions and replay](03-approval-revisions-and-replay.md)
    - [Compare workflow traces and handoffs](04-compare-workflow-traces-and-handoffs.md)

## What you will learn

Turn a small change request into regression and acceptance examples.

## Protect an old behavior on purpose

Whitespace should collapse in tickets. Empty inputs must still go to review. The first suggested change disregards the legacy behavior.

Write acceptance cases before implementation. Include a failing case that demonstrates the new requirement and a passing case for what people already expect.

## How it works

An acceptance case states an observable input and expected output. Freeze current behaviors you want to preserve before asking for a change, and keep acceptance cases independent from any particular implementation. A small fixture makes a failing example cheap to inspect.

### Write behavior before inviting implementation

An acceptance contract describes observable results for the proposed change, side effects, and old behavior the user still relies on. Build a small set that distinguishes the current implementation from the proposed one. A good starting set includes a normal input, a boundary case, and a preserved behavior.

For a formatter, “trim whitespace” leaves open whether internal spaces collapse and what happens when the result is empty. Use an input with both surrounding and internal spaces. An empty input can still go to the existing review mechanism. Test both so the proposed improvement cannot accidentally turn an unparseable ticket into an accepted one.

First run the tests against the current implementation. You expect the new case to fail for the reason you intend to fix, while existing cases pass. A test that already passes both implementations provides little evidence about the change. Keep the input and expected output in the review packet.

## Worked example

A task-title formatter should now remove redundant spaces. Existing lowercasing and empty-title behavior still matter. Add a fixture for tabs and a case that captures the default title.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def current_title(value):
    return value.strip().lower() or "untitled"


CASES = (
    (" Study PLAN ", "study plan"),
    ("", "untitled"),
    ("draft\t  release   plan", "draft release plan"),
)


def regressions(formatter):
    failures = []
    for value, expected in CASES:
        actual = formatter(value)
        if actual != expected:
            failures.append({"input": value, "expected": expected, "actual": actual})
    return failures


assert len(regressions(current_title)) == 1
```

## Try it yourself

Write one legacy case and one case that fails with the baseline.

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The whitespace case should reproduce the new requirement. The legacy case should remain green after the change.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Constrain proposals and run checks →](02-constrain-proposals-and-run-checks.md)
{: .study-directions .study-directions--footer }
