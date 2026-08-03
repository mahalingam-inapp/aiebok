"""Lab 12.2: Identity, Data, and Trust Boundaries"""

CHAPTER = "12.2"
print("chapter hook:", CHAPTER)
boundaries = ["user->gateway", "gateway->retrieval", "tool->HR API"]
for b in boundaries:
    print(b, "requires authZ check")
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
