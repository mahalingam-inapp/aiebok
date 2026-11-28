# Bounded search and independent verification

<p class="study-position" data-course="reasoning-efficient-inference" data-lecture="02-bounded-search-and-independent-verification.md">Allocate compute at inference time · Lecture 2 of 4</p>

[← Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md) · [Course outline](index.md#course-outline){ .study-overview } · [Prefill, decode and speculative decoding →](03-prefill-decode-and-speculative-decoding.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Allocate compute at inference time**

    - [Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md)
    - **Bounded search and independent verification** (current)

    **Improve throughput and measure honestly**

    - [Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md)
    - [Serving workload and release gates](04-serving-workload-and-release-gates.md)

## What you will learn

Select a valid answer from candidate outputs under a bounded attempt budget.

## Test the answer before reading the explanation

Two routes look reasonable in the planner's prose. One uses a closed lift and the other has a bad total.

Run an independent feasibility check over the structured routes. Track when a valid route is never proposed separately from when the verifier accepts a bad route.

## How it works

A generator proposes candidates, and a separate verifier checks observable conditions. For deterministic tasks, a test or solver can verify an answer. A learned judge adds another fallible estimate. Increasing sample count helps only when candidates add useful diversity and the verifier recognizes valid answers.

### A verifier can fail too
With a deterministic verifier, make the acceptance predicate part of the test suite. Use deliberately flawed candidates, including one whose stated answer is right while its action is infeasible. If a judge must read free text, calibrate it against human judgments and test whether irrelevant formatting or wording affects its labels. Track generator coverage, false acceptances, and out-of-budget cases separately.

## Worked example

A route planner proposes traces. The verifier checks which edges exist, whether any station is closed, and whether the reported total matches the route. A polished rationale cannot substitute for these checks.

### Follow the example

**Given:** Three candidates report [West, Lift, East] at cost 4, [West, East] at cost 6, and [West, East] at cost 7. The lift is closed, and the direct segment costs 7.

**Walkthrough:** The first is infeasible, the second misstates cost, and the third passes. A one-attempt budget abstains. Feasibility only certifies this route against the supplied contract.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
edges = {("West", "Lift"): 2, ("Lift", "East"): 2, ("West", "East"): 7}
proposals = [(("West", "Lift", "East"), 4), (("West", "East"), 6), (("West", "East"), 7)]


def choose_route(candidates, budget, closed):
    for nodes, total in candidates[:budget]:
        segments = list(zip(nodes, nodes[1:]))
        if len(nodes) < 2 or (nodes[0], nodes[-1]) != ("West", "East") or closed.intersection(nodes):
            continue
        if all(segment in edges for segment in segments) and sum(edges[edge] for edge in segments) == total:
            return nodes, total
    return None


assert choose_route(proposals, 1, {"Lift"}) is None
assert choose_route(proposals, 3, {"Lift"}) == (("West", "East"), 7)
print(choose_route(proposals, 3, {"Lift"}))
```

## Try it yourself

Add a plausible but infeasible candidate before a valid one. Compare the selection at budgets one and three.

[Download the workbook](../../assets/notebooks/reasoning-efficient-inference.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A budget of one may abstain. A larger budget can find a verified candidate. A feasibility check alone does not prove optimality.

## Continue

[← Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md) · [Course outline](index.md#course-outline){ .study-overview } · [Prefill, decode and speculative decoding →](03-prefill-decode-and-speculative-decoding.md)
{: .study-directions .study-directions--footer }
