"""Lab 12.6: Enterprise Operating Model"""

CHAPTER = "12.6"
print("chapter hook:", CHAPTER)
RACI = {"platform": "operate gateway", "product": "own use-case evals", "governance": "tier approvals"}
for role, duty in RACI.items():
    print(role, duty)
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
