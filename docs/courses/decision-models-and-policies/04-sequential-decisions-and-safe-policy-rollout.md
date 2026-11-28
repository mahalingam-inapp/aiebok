# Sequential decisions and safe policy rollout

<p class="study-position" data-course="decision-models-and-policies" data-lecture="04-sequential-decisions-and-safe-policy-rollout.md">Learn and evaluate from feedback · Lecture 4 of 4</p>

[← Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Design the decision layer**

    - [Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md)
    - [Constrained optimization and planning](02-constrained-optimization-and-planning.md)

    **Learn and evaluate from feedback**

    - [Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md)
    - **Sequential decisions and safe policy rollout** (current)

## What you will learn

Compare myopic choices with finite-horizon planning and set a release contract for feedback-driven policies.

## Saving minutes now can cost a visit later

A policy defers tricky jobs to improve today's completed jobs per hour. Repeat visits rise over the next reporting period.

Include future workload and unresolved work in the objective. Evaluate a candidate with a shadow workload and connect delayed outcomes to the original policy decision.

## How it works

A one-step reward can favor actions that make later outcomes worse. A Markov decision process represents state, actions, transition dynamics and reward. Offline reinforcement learning and return-conditioned sequence models such as Decision Transformer learn from trajectories. Prompting for a high return does not provide evidence for actions outside the training distribution. Delayed outcomes, missing feedback, and shifts in the data-collection policy can all distort release decisions.

### Account for actions that change what happens next
A one-step bandit ignores subsequent state. Planning with a transition model allows a choice now to change later workload and rewards. Offline trajectory methods need coverage for the sequences a policy might produce, and observational logs can omit important influences. For a pilot, freeze a baseline, decide which decisions stay with staff, and set clear guardrails on repeat visits or unresolved requests.

## Worked example

Deferring an inspection frees a slot immediately but increases the chance of a later repeat visit. A policy that counts only completed tasks per hour learns to defer expensive cases.

### Follow the example

**Given:** Deferring gives 3 units now and creates a repeat visit costing 5. Inspecting gives 1 now and leaves the job resolved.

**Walkthrough:** A one-period policy defers. A two-period policy with no discount compares −2 and 1 and inspects. Include repeat visits in the eval before changing the schedule.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
# Deterministic transitions for a two-period planning fixture.
transitions = {
    "pending": {"defer": (3, "repeat"), "inspect": (1, "resolved")},
    "repeat": {"revisit": (-5, "resolved")},
    "resolved": {"hold": (0, "resolved")},
}


def plan(state, horizon, discount=1.0):
    if horizon == 0:
        return 0.0, ()
    candidates = []
    for action, (immediate, following) in transitions[state].items():
        future, suffix = plan(following, horizon - 1, discount)
        candidates.append((immediate + discount * future, (action, *suffix)))
    return max(candidates)


assert plan("pending", 1)[1][0] == "defer"
assert plan("pending", 2)[1][0] == "inspect"
print("horizons one and two", plan("pending", 1), plan("pending", 2))
```

## Try it yourself

Compare immediate reward and two-step return in a small model. Specify what would block a pilot even if mean reward improves.

[Download the workbook](../../assets/notebooks/decision-models-and-policies.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    State the supported contexts, workload limits, critical outcomes and stop rule. A simulator or an offline estimate can justify a shadow evaluation only within its assumptions.

## Continue

[← Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
