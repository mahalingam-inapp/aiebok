from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    group: str
    slice: str
    text: str
    label: str


splits = {
    "train": (
        Record("a", "short", "wifi network disconnect", "network"),
        Record("a", "long", "wifi access point network slow", "network"),
        Record("b", "short", "router internet wifi", "network"),
        Record("c", "short", "projector screen dark", "display"),
        Record("d", "long", "screen projector flickers with cable", "display"),
    ),
    "validation": (
        Record("e", "short", "network wifi slow", "network"),
        Record("f", "short", "projector cable screen", "display"),
        Record("g", "long", "wifi classroom screen setup check", "display"),
    ),
    "test": (
        Record("h", "short", "router wifi down", "network"),
        Record("i", "long", "classroom projector screen dark today", "display"),
        Record("j", "short", "cable issue", "display"),
        Record("k", "long", "classroom needs attention before class", "network"),
    ),
}
dataset_version = "classroom-support-fixtures-v1"


def check_splits(partitions):
    owners = {}
    for name, records in partitions.items():
        for row in records:
            previous = owners.setdefault(row.group, name)
            assert previous == name, f"group {row.group} crosses {previous} and {name}"


check_splits(splits)
print({name: dict(Counter(row.slice for row in records)) for name, records in splits.items()})

# %%
import math
import re


def words(text):
    return re.findall(r"[a-z]+", text.lower())


def fit(records):
    labels = Counter(row.label for row in records)
    counts = {label: Counter() for label in labels}
    for row in records:
        counts[row.label].update(words(row.text))
    return {"labels": dict(labels), "counts": {label: dict(c) for label, c in counts.items()}}


def predict(model, text):
    labels, counts = model["labels"], model["counts"]
    vocabulary = {term for tokens in counts.values() for term in tokens}
    scores = {}
    for label, count in labels.items():
        likelihood_denominator = sum(counts[label].values()) + len(vocabulary)
        scores[label] = math.log(count / sum(labels.values())) + sum(
            math.log((counts[label].get(term, 0) + 1) / likelihood_denominator)
            for term in words(text) if term in vocabulary
        )
    best = max(sorted(scores), key=scores.get)
    confidence = 1 / sum(math.exp(score - scores[best]) for score in scores.values())
    return best, confidence


model = fit(splits["train"])
majority = max(sorted(model["labels"]), key=model["labels"].get)
for row in splits["validation"]:
    print(row.label, majority, predict(model, row.text))
assert sum(model["labels"].values()) == len(splits["train"])
assert predict(model, "projector screen")[0] == "display"

# %%
from collections import defaultdict


def evaluate(records, predictor, threshold, review_cost=1, error_cost=4):
    summary = defaultdict(Counter)
    for row in records:
        predicted, confidence = predictor(row.text)
        outcome = "handoff" if confidence < threshold else ("correct" if predicted == row.label else "wrong")
        summary["all"][outcome] += 1
        summary[row.slice][outcome] += 1
    result = {}
    for key, counts in summary.items():
        accepted = counts["correct"] + counts["wrong"]
        result[key] = {
            "n": counts.total(), "wrong_accepted": counts["wrong"], "handoffs": counts["handoff"],
            "coverage": accepted / counts.total(),
            "accepted_accuracy": counts["correct"] / accepted if accepted else None,
            "cost": review_cost * counts["handoff"] + error_cost * counts["wrong"],
        }
    return result


def trained(text):
    return predict(model, text)


thresholds = (0.5, 0.65, 0.8, 0.9)
validation = {t: evaluate(splits["validation"], trained, t)["all"] for t in thresholds}
threshold = min(thresholds, key=lambda t: (validation[t]["cost"], -validation[t]["coverage"], t))
baseline = evaluate(splits["test"], lambda text: (majority, 1), 0)
report = evaluate(splits["test"], trained, threshold)
print("Validation", validation)
print("Frozen threshold", threshold, "baseline", baseline, "test", report)
assert report["all"]["n"] == len(splits["test"])
assert report["all"]["cost"] < baseline["all"]["cost"]

# %%
import json
from pathlib import Path
from tempfile import TemporaryDirectory

artifact = {"dataset": dataset_version, "model_version": "nb-v1", "threshold": threshold, "parameters": model}
with TemporaryDirectory() as directory:
    artifact_path = Path(directory) / "classifier.json"
    artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
    restored = json.loads(artifact_path.read_text(encoding="utf-8"))

for row in splits["test"]:
    assert predict(restored["parameters"], row.text) == trained(row.text)

overall = report["all"]
release = (
    overall["coverage"] >= 0.5
    and overall["accepted_accuracy"] is not None
    and overall["accepted_accuracy"] >= 0.8
    and overall["cost"] < baseline["all"]["cost"]
)
print("Release decision for this fixture", "pass" if release else "hold", restored["model_version"])
