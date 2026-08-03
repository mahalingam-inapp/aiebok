"""Lab 8.5: Multi-Agent Systems"""

CHAPTER = "8.5"
print("chapter hook:", CHAPTER)
workers = {"A": "fetch HR policy", "B": "fetch IT policy"}
shared = []
for w, task in workers.items():
    shared.append({"worker": w, "result": f"evidence from {task}"})
conflicts = len({r["result"][:10] for r in shared}) < len(shared)
print({"evidence": shared, "conflict": conflicts})
print("---")
print("change one input above, predict output, re-run")
