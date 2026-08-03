"""Lab 2.1: Problems, Data, and Baselines"""

apps = [
    {"id": 1, "income": 80000, "decision": 1},
    {"id": 2, "income": 40000, "decision": 0},
    {"id": 3, "income": 120000, "decision": 1},
]
baseline_rate = sum(a["decision"] for a in apps) / len(apps)
pred = 1 if baseline_rate >= 0.5 else 0
acc = sum(pred == a["decision"] for a in apps) / len(apps)
print({"majority_pred": pred, "accuracy": round(acc, 3)})
