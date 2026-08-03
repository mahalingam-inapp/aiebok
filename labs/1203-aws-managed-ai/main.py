"""Lab 12.3: AWS Managed AI"""

CHAPTER = "12.3"
print("chapter hook:", CHAPTER)
mapping = {"models": "Bedrock", "search": "OpenSearch", "compute": "Lambda/EKS", "identity": "IAM"}
for cap, svc in mapping.items():
    print(f"{cap} -> {svc}")
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
