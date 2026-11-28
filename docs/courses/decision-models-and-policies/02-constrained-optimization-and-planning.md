# Constrained optimization and planning

<p class="study-position" data-course="decision-models-and-policies" data-lecture="02-constrained-optimization-and-planning.md">Design the decision layer · Lecture 2 of 4</p>

[← Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md) · [Course outline](index.md#course-outline){ .study-overview } · [Contextual bandits and off-policy evaluation →](03-contextual-bandits-and-off-policy-evaluation.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design the decision layer**

    - [Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md)
    - **Constrained optimization and planning** (current)

    **Learn and evaluate from feedback**

    - [Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md)
    - [Sequential decisions and safe policy rollout](04-sequential-decisions-and-safe-policy-rollout.md)

## What you will learn

Choose a feasible assignment under shared resources and compare it with greedy ranking.

## Several good jobs compete for one crew

The highest-value job needs both available time blocks. Two smaller jobs fit together and can be finished today.

Solve for the set of jobs rather than the rank of an individual ticket. If a compulsory job cannot fit, escalate the schedule instead of dropping it silently.

## How it works

When decisions share a constraint, a per-item score cannot choose the full action set. Represent choices as variables with an objective and explicit constraints. For small instances, exhaustive search is usable as a reference. For larger instances, a solver such as CP-SAT can optimize discrete assignments under a time limit. For sequential choices, planning adds transitions and a horizon.

### Separate feasibility from performance
Start with a tiny instance where you can enumerate every plan and verify the optimum. Then use variables for task inclusion, precedence, and assignment as you extend the model. Evaluate a greedy baseline against the same rules. For a bigger solver, record objective value, bounds, elapsed time, and status. Defining who handles an infeasible instance matters when the plan determines real work.

## Worked example

One job pays 9 units and occupies both available slots. Two smaller jobs pay 6 units each and fit together. Taking the highest-value single job leaves three units of value on the table.

### Follow the example

**Given:** Two technician slots are free. Job A takes both slots for benefit 9. Jobs B and C each take one slot and yield 6.

**Walkthrough:** Enumerate feasible sets. B and C yield 12 together. If A is mandatory, it becomes the feasible optimum. Record infeasibility explicitly when mandatory jobs exceed capacity.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from itertools import combinations

jobs = (("large", 2, 9), ("small-a", 1, 6), ("small-b", 1, 6))


def assign(jobs, capacity, required=()):
    feasible = (
        (sum(value for _, _, value in subset), tuple(name for name, _, _ in subset))
        for size in range(len(jobs) + 1)
        for subset in combinations(jobs, size)
        if sum(slots for _, slots, _ in subset) <= capacity
        and set(required) <= {name for name, _, _ in subset}
    )
    return max(feasible, default=None)


def greedy(jobs, capacity):
    value = 0
    for _, slots, benefit in sorted(jobs, key=lambda job: -job[2]):
        if slots <= capacity:
            value += benefit
            capacity -= slots
    return value


assert assign(jobs, 2) == (12, ("small-a", "small-b"))
assert assign(jobs, 1, {"large"}) is None
for capacity in (1, 2):
    print("capacity", capacity, "greedy", greedy(jobs, capacity), "optimal", assign(jobs, capacity))
```

## Try it yourself

Compare greedy and exhaustive assignment under two capacity settings. Add a mandatory task and report infeasibility when it cannot fit.

[Download the workbook](../../assets/notebooks/decision-models-and-policies.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Enforce capacity and required tasks before comparing objective values. In production, report a feasible incumbent and solver status when the time limit prevents proving optimality.

## Continue

[← Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md) · [Course outline](index.md#course-outline){ .study-overview } · [Contextual bandits and off-policy evaluation →](03-contextual-bandits-and-off-policy-evaluation.md)
{: .study-directions .study-directions--footer }
