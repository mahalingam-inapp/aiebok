"""Lab 10.4: Security of AI Systems"""

CHAPTER = "10.4"
print("chapter hook:", CHAPTER)
attacks = ["inject retrieved", "exfil via markdown", "tool arg injection"]
mitigations = {"inject retrieved": "data labeling", "exfil via markdown": "output filter", "tool arg injection": "schema + sandbox"}
for a in attacks:
    print(a, "->", mitigations[a])
print("---")
print("change one input above, predict output, re-run")
