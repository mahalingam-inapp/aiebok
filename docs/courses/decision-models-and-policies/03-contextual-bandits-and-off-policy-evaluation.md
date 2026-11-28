# Contextual bandits and off-policy evaluation

<p class="study-position" data-course="decision-models-and-policies" data-lecture="03-contextual-bandits-and-off-policy-evaluation.md">Learn and evaluate from feedback · Lecture 3 of 4</p>

[← Constrained optimization and planning](02-constrained-optimization-and-planning.md) · [Course outline](index.md#course-outline){ .study-overview } · [Sequential decisions and safe policy rollout →](04-sequential-decisions-and-safe-policy-rollout.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Design the decision layer**

    - [Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md)
    - [Constrained optimization and planning](02-constrained-optimization-and-planning.md)

    **Learn and evaluate from feedback**

    - **Contextual bandits and off-policy evaluation** (current)
    - [Sequential decisions and safe policy rollout](04-sequential-decisions-and-safe-policy-rollout.md)

## What you will learn

Estimate a target policy from logged actions, rewards and propensities while checking support.

## History contains the actions somebody chose

The log has thousands of observations, but a rarely selected region has very little evidence for the new policy's proposed action.

Record the logging policy's action probabilities and measure overlap. Examine effective sample size and stop the comparison if the target action has no historical support.

## How it works

A contextual bandit observes context, chooses one action and receives feedback for that action. Logged outcomes are therefore selected by the behavior policy. Inverse propensity scoring reweights a logged reward by target probability divided by logging probability. For a deterministic target, the numerator is an indicator. A policy that chooses actions with zero logging probability cannot be evaluated this way in those contexts.

### Check overlap before reporting value
A log provides a reward only for the action it took. A deterministic target puts weight only on matching logged actions, but it requires support for its chosen action in every context being evaluated. Compute effective sample size as the squared sum of weights divided by their sum of squares. A confidence interval or sensitivity analysis is more informative than extra decimal places. If the logger's probabilities were never recorded, an assumed replay estimator may tell you more about the assumptions than the policy.

## Worked example

When an action has probability one quarter under the logger and the new policy always chooses it, a matching action contributes weight four. High weights can make a few examples dominate the estimate.

### Follow the example

**Given:** A four-row log chooses the target action once with logging probability 0.25, and that row has reward 1.

**Walkthrough:** The inverse propensity estimate is (4 × 1) ÷ 4 = 1, with an effective sample size of 1. Withhold a confident policy comparison. If any target action has zero support, the estimator cannot cover that context.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def ips(rows):
    # Row fields: logged action, reward, full logging probabilities, target action.
    if not rows or any(probabilities.get(target, 0) <= 0 for _, _, probabilities, target in rows):
        return None
    weights = [1 / probabilities[target] if action == target else 0
               for action, _, probabilities, target in rows]
    estimate = sum(weight * row[1] for weight, row in zip(weights, rows)) / len(rows)
    squares = sum(weight ** 2 for weight in weights)
    effective_size = sum(weights) ** 2 / squares if squares else 0
    return estimate, effective_size


logged = [("A", 1, {"A": 0.25, "B": 0.75}, "A"),
          ("B", 1, {"A": 0.25, "B": 0.75}, "A"),
          ("B", 0, {"A": 0.25, "B": 0.75}, "A"),
          ("B", 0, {"A": 0.25, "B": 0.75}, "A")]
assert ips(logged) == (1.0, 1.0)
assert ips([("B", 1, {"B": 1.0}, "A")]) is None
print("IPS and effective sample size", ips(logged))
```

## Try it yourself

Compute the weighted mean and effective sample size, then set one required logging probability to zero.

[Download the workbook](../../assets/notebooks/decision-models-and-policies.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The estimate must report missing support even if the logged action on that row is different. Doubly robust estimators can also use a reward model. Validate their assumptions before comparing policies.

## Continue

[← Constrained optimization and planning](02-constrained-optimization-and-planning.md) · [Course outline](index.md#course-outline){ .study-overview } · [Sequential decisions and safe policy rollout →](04-sequential-decisions-and-safe-policy-rollout.md)
{: .study-directions .study-directions--footer }
