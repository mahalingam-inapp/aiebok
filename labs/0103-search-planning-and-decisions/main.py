"""Lab 1.3: Search, Planning, and Decisions"""

GRAPH = {"start": ["oncall_a", "oncall_b"], "oncall_a": ["lead"], "oncall_b": ["lead"], "lead": []}
GOAL = "lead"
def bfs(start, goal):
    queue = [(start, [start])]
    seen = {start}
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        for nxt in GRAPH.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None
print("escalation path:", bfs("start", GOAL))
