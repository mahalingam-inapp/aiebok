"""Lab 12.1: Enterprise AI Building Blocks"""

CHAPTER = "12.1"
print("chapter hook:", CHAPTER)
capabilities = ["gateway", "retrieval", "tool registry", "identity", "observability"]
products = {"aws": "bedrock", "azure": "foundry", "gcp": "vertex"}
for cap in capabilities:
    print(cap, "maps to provider-specific service behind interface")
print("---")
print("change one input above, predict output, re-run")
