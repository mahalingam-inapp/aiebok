# Calibrated predictions and decisions under cost

<p class="study-position" data-course="decision-models-and-policies" data-lecture="01-calibrated-predictions-and-decisions-under-cost.md">Design the decision layer · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Constrained optimization and planning →](02-constrained-optimization-and-planning.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design the decision layer**

    - **Calibrated predictions and decisions under cost** (current)
    - [Constrained optimization and planning](02-constrained-optimization-and-planning.md)

    **Learn and evaluate from feedback**

    - [Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md)
    - [Sequential decisions and safe policy rollout](04-sequential-decisions-and-safe-policy-rollout.md)

## What you will learn

Derive an action threshold from costs and measure the option to defer.

## Give the uncertainty somewhere to go

A maintenance alert is neither clearly routine nor obviously urgent. The model is moderately confident and a short review is available.

Write the action and review costs before choosing a threshold. Track how often the policy defers and whether the team can handle that load.

## How it works

A predictive model estimates outcomes. A policy chooses an action given the estimate, constraints and consequences. For binary action with two wrong-decision costs and zero cost for correct decisions, act when the probability exceeds the false-positive cost divided by the sum of error costs. Deferral adds a third option with its own cost and capacity. A reliability diagram checks calibration across groups of forecasts.

### Put utility above the score
Write a table of actions and their costs conditional on each outcome. Take expectations using the estimated probability, then compare these expected costs with a review option. On historical cases, measure realized outcomes and costs separately. Compare calibration by slice because a score can be calibrated overall and biased in a smaller group. If the options consume shared reviewer time, defer thresholds alone cannot enforce that budget.

## Worked example

If unnecessary dispatch costs 2 and a missed issue costs 8, the two-action threshold is 0.2. A low-cost review step can be preferable to either action for some scores.

### Follow the example

**Given:** The urgency estimate is 0.19. Unnecessary action costs 2, a missed issue costs 8, and review costs 0.50.

**Walkthrough:** Expected action cost is 1.62, waiting costs 1.52, and review costs 0.50. Choose review while a reviewer has capacity. This calculation assumes review resolves the uncertainty at the stated cost.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from collections import Counter


def choose_action(probability, review_cost, false_positive=2, false_negative=8):
    costs = {"act": (1 - probability) * false_positive, "wait": probability * false_negative,
             "review": review_cost}
    return min(costs, key=costs.get)


cases = [(0.1, 0), (0.19, 1), (0.4, 0), (0.85, 1)]
for review_cost in (0.5, 1.5, 2.0):
    actions = [choose_action(score, review_cost) for score, _ in cases]
    realized = sum(
        review_cost if action == "review" else 2 * (1 - truth) if action == "act" else 8 * truth
        for action, (_, truth) in zip(actions, cases)
    )
    print(review_cost, Counter(actions), realized)
for low, high in ((0, 0.25), (0.25, 0.75), (0.75, 1.01)):
    bucket = [(score, truth) for score, truth in cases if low <= score < high]
    if bucket:
        print("calibration bucket", (low, high), "count", len(bucket),
              "mean forecast", sum(score for score, _ in bucket) / len(bucket),
              "observed rate", sum(truth for _, truth in bucket) / len(bucket))
print("Brier score", sum((score - truth) ** 2 for score, truth in cases) / len(cases))
assert choose_action(0.19, 2) == "wait"
assert choose_action(0.19, 0.5) == "review"
```

## Try it yourself

Change the review cost and compare decisions, realized losses, and calibration on the same cases.

[Download the workbook](../../assets/notebooks/decision-models-and-policies.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Lower review cost expands the range where review is attractive. Calibration quality and policy value are different measures.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Constrained optimization and planning →](02-constrained-optimization-and-planning.md)
{: .study-directions .study-directions--footer }
