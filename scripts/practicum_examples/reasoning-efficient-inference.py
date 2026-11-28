# These fixtures describe verification results, not sampled model responses.
requests = [(True, True), (True, True), (False, True), (False, False)]


def trial(rows, mode):
    verified = spend = escalations = 0
    for cheap, expensive in rows:
        if mode == "expensive":
            spend += 4
            verified += expensive
            continue
        spend += 1
        if mode == "cascade" and not cheap:
            escalations += 1
            spend += 4
            verified += expensive
        else:
            verified += cheap
    return verified, spend, escalations


for mode in ("cheap", "expensive", "cascade"):
    print(mode, trial(requests, mode))
assert trial(requests, "cascade") == (3, 12, 2)
# %%
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
# %%
def greedy_speculation(draft, target):
    """One check. Target must supply a token for each position verified."""
    if len(target) < len(draft):
        raise ValueError("Missing target tokens")
    for index, token in enumerate(draft):
        if token != target[index]:
            return tuple(draft[:index]) + (target[index],), index
    return tuple(draft), len(draft)


assert greedy_speculation(("a", "b", "x", "d"), ("a", "b", "c", "z")) == (("a", "b", "c"), 2)
assert greedy_speculation(("a", "b"), ("a", "b")) == (("a", "b"), 2)
print(greedy_speculation(("a", "b", "x", "d"), ("a", "b", "c", "z")))
# %%
from math import ceil


def p95(observations):
    return sorted(observations)[ceil(0.95 * len(observations)) - 1]


# Synthetic milliseconds. Pooling makes the smaller cohort's failure disappear.
warm = [85] * 100
cold = [140, 210, 310]
limit = 200
assert p95(warm + cold) <= limit < p95(cold)
print("p95 TTFT by cohort", {"warm": p95(warm), "cold": p95(cold), "pooled": p95(warm + cold)})
