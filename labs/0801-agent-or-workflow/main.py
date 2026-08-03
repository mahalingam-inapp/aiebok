"""Lab 8.1: Agent or Workflow?"""

WORKFLOW = ["create_account", "assign_laptop", "grant_access"]
AGENT = {"goal": "complete onboarding", "actions": WORKFLOW, "replans": True}
def run(steps, fail_at=None):
    done = []
    for i, s in enumerate(steps):
        if fail_at == i:
            return done, "paused"
        done.append(s)
    return done, "complete"
print("workflow:", run(WORKFLOW, fail_at=1))
print("agent can resume:", AGENT["replans"])
