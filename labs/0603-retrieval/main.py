"""Lab 6.3: Retrieval"""

CHAPTER = "6.3"
print("chapter hook:", CHAPTER)
docs = {"a": "PTO accrual cap is 240 hours", "b": "Leave policy overview"}
query = set("pto cap".split())
scores = {k: len(query & set(v.lower().split())) for k, v in docs.items()}
print("bm25_proxy:", sorted(scores.items(), key=lambda x: -x[1]))
print("---")
print("change one input above, predict output, re-run")
