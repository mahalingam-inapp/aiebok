"""Lab 3.6: Embedding Systems in Production"""

eval_set = [
    {"q": "PTO carryover", "gold": "doc-leave-2024", "lang": "en"},
    {"q": "congé report", "gold": "doc-leave-fr", "lang": "fr"},
]
model_versions = {"v1": 0.82, "v2": 0.71}
for row in eval_set:
    score = model_versions["v2"] if row["lang"] == "fr" else model_versions["v1"]
    print({"query": row["q"], "ndcg_proxy": score, "pass": score >= 0.75})
