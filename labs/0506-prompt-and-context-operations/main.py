"""Lab 5.6: Prompt and Context Operations"""

CHAPTER = "5.6"
print("chapter hook:", CHAPTER)
prompts = {"v1.3": {"success": 0.84}, "v1.4": {"success": 0.81}}
active = "v1.3"
candidate = "v1.4"
gate = 0.02
delta = prompts[candidate]["success"] - prompts[active]["success"]
decision = "promote" if delta >= -gate else "rollback"
print({"active": active, "candidate": candidate, "delta": round(delta, 3), "decision": decision})
print("---")
print("change one input above, predict output, re-run")
