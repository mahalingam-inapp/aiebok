"""Lab 5.4: Conversation and Memory"""

memories = [
    {"text": "Approved WFH stipend", "score": 0.9, "source": "db"},
    {"text": "User likes concise answers", "score": 0.4, "source": "summary"},
]
query = "WFH stipend approval"
def relevance(m, q):
    return m["score"] * (1 if any(w in m["text"].lower() for w in q.lower().split()) else 0.2)
ranked = sorted(memories, key=lambda m: -relevance(m, query))
print("selected:", ranked[0])
