"""Compare breadth-first search and A* on the same grid."""
from collections import deque
from heapq import heappop, heappush

GRID = ["S...#", ".##..", "...#.", ".#...", "...G."]
START, GOAL = (0, 0), (4, 3)


def neighbors(node):
    r, c = node
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(GRID) and 0 <= nc < len(GRID[0]) and GRID[nr][nc] != "#":
            yield nr, nc


def reconstruct(parent, node):
    path = [node]
    while node in parent:
        node = parent[node]
        path.append(node)
    return list(reversed(path))


def bfs():
    queue, parent, seen = deque([START]), {}, {START}
    expanded = 0
    while queue:
        node = queue.popleft(); expanded += 1
        if node == GOAL:
            return reconstruct(parent, node), expanded
        for nxt in neighbors(node):
            if nxt not in seen:
                seen.add(nxt); parent[nxt] = node; queue.append(nxt)


def astar():
    frontier, parent, cost = [(0, START)], {}, {START: 0}
    expanded = 0
    while frontier:
        _, node = heappop(frontier); expanded += 1
        if node == GOAL:
            return reconstruct(parent, node), expanded
        for nxt in neighbors(node):
            new_cost = cost[node] + 1
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost; parent[nxt] = node
                heuristic = abs(nxt[0] - GOAL[0]) + abs(nxt[1] - GOAL[1])
                heappush(frontier, (new_cost + heuristic, nxt))


if __name__ == "__main__":
    for name, search in (("BFS", bfs), ("A*", astar)):
        path, expanded = search()
        print(f"{name}: path_length={len(path)-1}, expanded={expanded}, path={path}")
