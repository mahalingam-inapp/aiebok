"""Lab 7.1: Reasoning as Search"""

states = [("start", ["search US", "search CA"]), ("search US", ["merge"]), ("search CA", ["merge"])]
budget = 3
expanded = 0
agenda = ["start"]
while agenda and expanded < budget:
    node = agenda.pop(0)
    expanded += 1
    next_nodes = dict(states).get(node, [])
    agenda.extend(next_nodes)
print({"expanded": expanded, "remaining": agenda})
