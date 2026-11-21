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

# %%
def agreement(left, right):
    pairs = list(zip(left, right, strict=True))
    observed = sum(a == b for a, b in pairs) / len(pairs)
    yes_left, yes_right = sum(left) / len(left), sum(right) / len(right)
    chance = yes_left * yes_right + (1 - yes_left) * (1 - yes_right)
    return observed, (observed - chance) / (1 - chance) if chance != 1 else None


reviewer_1 = [1, 1, 0, 0, 0, 1]
reviewer_2 = [1, 1, 0, 0, 1, 1]
observed, kappa = agreement(reviewer_1, reviewer_2)
print("Disagreement indices", [i for i, pair in enumerate(zip(reviewer_1, reviewer_2)) if pair[0] != pair[1]])
print("Agreement", observed, "Cohen kappa", kappa)
assert abs(kappa - 2 / 3) < 1e-9
assert agreement([1, 1], [1, 1]) == (1, None)

# %%
from random import Random
from statistics import median, quantiles


def fixture(excluded, latency, spend):
    return {
        case.id: ("bad" if case.id in excluded else case.expected, latency, spend / len(cases))
        for case in cases
    }


candidates = {
    "Fast": fixture({"payroll"}, 420, 0.012),
    "Balanced": fixture({"parking"}, 680, 0.026),
    "Careful": fixture(set(), 1100, 0.051),
}


def report(outputs):
    correct = [outputs[case.id][0] == case.expected for case in cases]
    spend = sum(outputs[case.id][2] for case in cases)
    slices = {
        name: (sum(ok for ok, case in zip(correct, cases) if case.slice == name),
               sum(case.slice == name for case in cases))
        for name in sorted({case.slice for case in cases})
    }
    return {"correct": correct, "slices": slices, "latency": median(r[1] for r in outputs.values()),
            "cost_per_correct": spend / sum(correct) if any(correct) else None}


def paired_interval(candidate, baseline, seed=14):
    deltas = [int(a) - int(b) for a, b in zip(candidate, baseline, strict=True)]
    rng = Random(seed)
    draws = sorted(sum(rng.choices(deltas, k=len(deltas))) / len(deltas) for _ in range(2000))
    bounds = quantiles(draws, n=40, method="inclusive")
    return sum(deltas) / len(deltas), (bounds[0], bounds[-1])


reports = {name: report(rows) for name, rows in candidates.items()}
print("Balanced minus Fast", paired_interval(reports["Balanced"]["correct"], reports["Fast"]["correct"]))
assert reports["Fast"]["slices"]["critical"] == (1, 2)
assert reports["Careful"]["slices"]["critical"] == (2, 2)
assert paired_interval(reports["Fast"]["correct"], reports["Fast"]["correct"]) == (0, (0, 0))

# %%
def select(reports, latency_limit=800):
    eligible = [
        name for name, row in reports.items()
        if row["slices"]["critical"] == (2, 2)
        and row["latency"] <= latency_limit
        and row["cost_per_correct"] is not None
    ]
    return min(eligible, key=lambda name: reports[name]["cost_per_correct"], default=None)


assert select(reports) == "Balanced"
assert select(reports, latency_limit=650) is None
print("Selection for this fixture:", select(reports))
