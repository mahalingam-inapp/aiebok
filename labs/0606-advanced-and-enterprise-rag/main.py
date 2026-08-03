"""Lab 6.6: Advanced and Enterprise RAG"""

CHAPTER = "6.6"
print("chapter hook:", CHAPTER)
routes = {"simple": {"hops": 1, "cost": 1}, "multi": {"hops": 3, "cost": 4}}
def adaptive(query):
    return "multi" if "and also" in query or "depending on" in query else "simple"
queries = ["PTO cap?", "PTO cap and carryover depending on tenure"]
for q in queries:
    r = adaptive(q)
    print({"query": q, "route": r, "cost_units": routes[r]["cost"]})
print("---")
print("change one input above, predict output, re-run")
