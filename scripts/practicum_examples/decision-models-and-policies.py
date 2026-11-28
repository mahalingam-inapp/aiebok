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
# %%
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
# %%
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
# %%
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
