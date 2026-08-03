"""Lab 13.5: Long Context, World Models, and Continual Learning"""

CHAPTER = "13.5"
print("chapter hook:", CHAPTER)
methods = {"long_context": 0.88, "rag": 0.91, "explicit_state": 0.89}
cost = {"long_context": 9, "rag": 3, "explicit_state": 2}
print({m: {"acc": methods[m], "cost": cost[m]} for m in methods})
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
