"""Generate candidate plans, verify constraints, and select the cheapest valid plan."""
PLANS = [
    ["read", "publish"],
    ["read", "draft", "review", "publish"],
    ["draft", "read", "publish"],
]


def verify(plan):
    required = {"read", "draft", "review", "publish"}
    if not required.issubset(plan): return False, "missing required step"
    positions = {step: plan.index(step) for step in required}
    if not positions["read"] < positions["draft"] < positions["review"] < positions["publish"]:
        return False, "invalid dependency order"
    return True, "valid"


valid = []
for plan in PLANS:
    ok, reason = verify(plan); print(plan, ok, reason)
    if ok: valid.append(plan)
print("selected=", min(valid, key=len))
