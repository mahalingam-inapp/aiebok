"""Lab 11.5: Deployment and Routing"""

CHAPTER = "11.5"
print("chapter hook:", CHAPTER)
options = {"hosted": {"control": 2, "cost": 3}, "self": {"control": 5, "cost": 4}}
need = "data residency strict"
choice = "self" if "residency" in need else "hosted"
print({"choice": choice, **options[choice]})
print("---")
print("change one input above, predict output, re-run")
