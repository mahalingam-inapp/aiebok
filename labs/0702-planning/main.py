"""Lab 7.2: Planning"""

steps = {"fetch_US": [], "fetch_CA": [], "compare": ["fetch_US", "fetch_CA"], "draft": ["compare"]}
def valid_plan(completed):
    for step, prereqs in steps.items():
        if step in completed and not all(p in completed for p in prereqs):
            return False, step
    return True, "ok"
completed = {"fetch_US", "compare"}
print(valid_plan(completed))
