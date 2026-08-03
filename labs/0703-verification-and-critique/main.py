"""Lab 7.3: Verification and Critique"""

candidates = [
    {"text": "Cap is 240", "cite_ok": True, "score": 0.7},
    {"text": "Cap is 300", "cite_ok": False, "score": 0.9},
]
def select(cands):
    passing = [c for c in cands if c["cite_ok"]]
    return max(passing, key=lambda c: c["score"]) if passing else None
print("selected:", select(candidates))
