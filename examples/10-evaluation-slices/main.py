"""Calculate overall and slice metrics with risk-specific release gates."""
CASES = [
    ("general", True), ("general", True), ("general", False),
    ("high-risk", True), ("high-risk", True),
]


def accuracy(rows): return sum(ok for _, ok in rows) / len(rows)
overall = accuracy(CASES)
slices = {name: accuracy([row for row in CASES if row[0] == name]) for name in {name for name, _ in CASES}}
release = overall >= 0.75 and slices["high-risk"] == 1.0
print("overall=", round(overall, 3), "slices=", slices, "release=", release)
raise SystemExit(0 if release else 1)
