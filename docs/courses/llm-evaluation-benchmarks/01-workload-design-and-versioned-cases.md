# Workload design and versioned cases

<p class="study-position" data-course="llm-evaluation-benchmarks" data-lecture="01-workload-design-and-versioned-cases.md">Design trustworthy evidence · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Rubrics and human agreement →](02-rubrics-and-human-agreement.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design trustworthy evidence**

    - **Workload design and versioned cases** (current)
    - [Rubrics and human agreement](02-rubrics-and-human-agreement.md)

    **Measure and decide**

    - [Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md)
    - [Release gates and selection memo](04-release-gates-and-selection-memo.md)

## What you will learn

Freeze a workload containing expected outcomes, critical slices, and realistic negative cases.

## Freeze the workload before asking who wins

Teams keep adding examples after seeing candidate mistakes. The more examples they add, the harder it becomes to interpret relative improvements.

Separate exploratory cases from a frozen comparison set with versioned provenance and critical slices. Evaluate the same inputs for all models. New discoveries can inform the next round without changing the meaning of this one.

## How it works

A paired benchmark uses the same inputs for every candidate. Store intended behavior, source provenance, slice labels, and versions so results remain comparable. Keep iteration cases separate from the final held-out set.

### Preserve comparability as the workload grows

A benchmark is a specified workload and scoring procedure. Freeze inputs, allowed evidence, expected behaviors, and the environment before measuring alternatives. Record an identifier for the set so another reviewer can tell whether a change in results came from the model or from different cases.

Separate exploratory inputs from a comparison set. Exploratory cases reveal failures and guide fixes. If you tune repeatedly on the reporting set, it becomes part of training by another route. Add a new, representative set before using the result to justify a wider release.

Include standard cases and critical slices such as missing evidence or a required handoff. Report the denominator per slice. Combining all cases can answer how a candidate performed on this mixture, but it cannot establish competence in a rare behavior for which the data offers little evidence.

## Worked example

A support assistant may answer a routine question, decline an unknown one, or withhold restricted information. Use fixtures that make each decision observable.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from dataclasses import asdict, dataclass
from hashlib import sha256
import json


@dataclass(frozen=True)
class Case:
    id: str
    slice: str
    expected: str


cases = (
    Case("travel", "routine", "answer"), Case("leave", "routine", "answer"),
    Case("room", "routine", "answer"), Case("hours", "routine", "answer"),
    Case("supplies", "routine", "answer"), Case("printer", "routine", "answer"),
    Case("snow", "unknown", "abstain"), Case("parking", "unknown", "abstain"),
    Case("payroll", "critical", "abstain"), Case("employee-record", "critical", "abstain"),
)


def fingerprint(rows):
    return sha256(json.dumps([asdict(row) for row in rows], sort_keys=True).encode()).hexdigest()[:12]


print("Fixture revision", fingerprint(cases), "N", len(cases))
assert fingerprint(cases) != fingerprint(cases + (Case("tax", "unknown", "abstain"),))
```

## Try it yourself

Inspect the case manifest and fingerprint. Add one abstention case and compare the fingerprint.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The dataset fingerprint changes and the added case has an explicit expected behavior and slice.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Rubrics and human agreement →](02-rubrics-and-human-agreement.md)
{: .study-directions .study-directions--footer }
