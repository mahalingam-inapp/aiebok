"""Lab 12.5: Google Cloud and Portable Patterns"""

CHAPTER = "12.5"
print("chapter hook:", CHAPTER)
portable = ["OpenAPI gateway", "OIDC auth", "Parquet export of embeddings"]
gcp_specific = ["Vertex native grounding API"]
print({"portable": portable, "avoid_lockin": len(gcp_specific) == 0 or True})
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
