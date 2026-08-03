"""Lab 11.6: LLMOps"""

CHAPTER = "11.6"
print("chapter hook:", CHAPTER)
canary = {"success_rate": 0.79, "baseline": 0.85, "threshold": -0.03}
delta = canary["success_rate"] - canary["baseline"]
action = "rollback" if delta < canary["threshold"] else "promote"
print({"delta": round(delta, 3), "action": action})
print("---")
print("change one input above, predict output, re-run")
