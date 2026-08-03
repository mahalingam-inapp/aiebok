"""Lab 10.6: Governance and Assurance"""

CHAPTER = "10.6"
print("chapter hook:", CHAPTER)
tiers = {1: ["model card"], 2: ["model card", "eval report", "rollback plan"]}
feature = "onboarding assistant"
tier = 2
print({"required": tiers[tier]})
print("---")
print("change one input above, predict output, re-run")
