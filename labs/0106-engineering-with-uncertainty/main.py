"""Lab 1.6: Engineering with Uncertainty"""

scores = [0.92, 0.61, 0.48, 0.33]
COST = {"fp": 200, "fn": 50000}
def expected_cost(threshold):
    decisions = [s >= threshold for s in scores]
    truth = [True, True, False, False]
    fp = sum(d and not t for d, t in zip(decisions, truth))
    fn = sum(not d and t for d, t in zip(decisions, truth))
    return fp * COST["fp"] + fn * COST["fn"]
for t in [0.5, 0.6, 0.7, 0.8]:
    print(f"threshold={t} expected_cost={expected_cost(t)}")
