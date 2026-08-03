"""Lab 8.3: Agent Memory and Recovery"""

checkpoints = []
state = {"step": "assign_laptop", "order_id": None}
def save(state):
    checkpoints.append(dict(state))
def resume():
    return checkpoints[-1] if checkpoints else None
save({"step": "create_account", "done": True})
state = resume()
print("resume_at:", state)
