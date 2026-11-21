from dataclasses import dataclass
from statistics import median


@dataclass(frozen=True)
class Trace:
    cohort: str
    version: str
    stages_ms: tuple[tuple[str, int], ...]
    valid: bool
    failed_at: str | None = None
    cost: float = 0.002

    @property
    def elapsed(self):
        return sum(value for _, value in self.stages_ms)


def trace(cohort, version, bad=False):
    return Trace(cohort, version, (("retrieval", 20), ("generation", 900 if bad else 180), ("validation", 15)),
                 not bad, "generation" if bad else None)


stable = [trace("control", "v1") for _ in range(20)]
healthy = [trace("pilot", "v2") for _ in range(20)]
unhealthy = [trace("pilot", "v2", bad=i < 4) for i in range(20)]


def objectives(rows, latency_limit=350, target=0.99):
    good = sum(row.valid and row.elapsed <= latency_limit for row in rows)
    bad_fraction = (len(rows) - good) / len(rows)
    return {"n": len(rows), "good": good, "burn": bad_fraction / (1 - target),
            "median_ms": median(row.elapsed for row in rows), "mean_cost": sum(row.cost for row in rows) / len(rows)}


assert objectives(stable)["burn"] == 0
assert abs(objectives(unhealthy)["burn"] - 20) < 1e-8

# %%
from collections import Counter


def failure_stages(rows):
    return Counter(row.failed_at for row in rows if row.failed_at)


assert failure_stages(stable) == {}
assert failure_stages(unhealthy) == {"generation": 4}
print("First failing stage", failure_stages(unhealthy).most_common(1))

# %%
def gate(rows, sample=20, burn_limit=2, latency_limit=350, cost_limit=0.003):
    if len(rows) < sample:
        return ["coverage"]
    info = objectives(rows)
    limits = (
        ("error_budget", info["burn"], burn_limit), ("latency", info["median_ms"], latency_limit),
        ("cost", info["mean_cost"], cost_limit),
    )
    return [name for name, observed, limit in limits if observed > limit]


assert gate(healthy) == []
assert gate(healthy[:1]) == ["coverage"]
assert gate(unhealthy) == ["error_budget"]
assert gate(unhealthy, burn_limit=21, cost_limit=0.001) == ["cost"]

# %%
class Rollout:
    def __init__(self, baseline, candidate):
        self.baseline = baseline
        self.candidate = candidate

    def route(self, cohort):
        return self.candidate if cohort == "pilot" and self.candidate else self.baseline

    def rollback(self):
        self.candidate = None


rollout = Rollout("v1", "v2")
assert rollout.route("pilot") == "v2"
timeline = [(0, "canary started", "v2"), (5, "error-budget gate blocked", gate(unhealthy))]
rollout.rollback()
timeline.append((6, "candidate disabled", rollout.route("pilot")))
smoke = trace("pilot", rollout.route("pilot"))
assert smoke.version == "v1" and smoke.valid and smoke.elapsed <= 350
timeline.append((7, "smoke checked", {"version": smoke.version, "elapsed_ms": smoke.elapsed}))
assert [minute for minute, _, _ in timeline] == sorted(minute for minute, _, _ in timeline)
print("Incident timeline", timeline)
print("Follow-up: service owner reproduces the dependency timeout in pre-release checks.")
