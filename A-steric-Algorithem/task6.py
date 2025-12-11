from heapq import heappush, heappop
import time
import math


def manhattan(state, goal):
    distance = 0
    for i in range(1, 16):
        x1, y1 = divmod(state.index(i), 4)
        x2, y2 = divmod(goal.index(i), 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def euclidean(state, goal):
    distance = 0
    for i in range(1, 16):
        x1, y1 = divmod(state.index(i), 4)
        x2, y2 = divmod(goal.index(i), 4)
        distance += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


def neighbor(state):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    moves = []

    idx = state.index(0)
    x, y = divmod(idx, 4)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            new_idx = nx * 4 + ny
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            moves.append(new_state)

    return moves



def a_star(initial, goal, heuristic_func):

    visited = set()
    pq = []
    nodes_explored = 0

    heappush(pq, (0, initial, []))

    start_time = time.time()

    while pq:
        f, current, path = heappop(pq)
        nodes_explored += 1

        if current == goal:
            total_time = time.time() - start_time
            return {
                "path": path,
                "path_length": len(path),
                "nodes_explored": nodes_explored,
                "time": total_time
            }

        visited.add(tuple(current))

        for move in neighbor(current):
            if tuple(move) not in visited:
                new_path = path + [move]
                g = len(new_path)
                h = heuristic_func(move, goal)
                heappush(pq, (g + h, move, new_path))

    return None



initial = [
    5, 1, 2, 4,
    9, 6, 3, 8,
    0, 10, 7, 12,
    13, 14, 11, 15
]

goal = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9,10,11,12,
    13,14,15, 0
]


print("Running A* with Manhattan Heuristic...")
res_m = a_star(initial, goal, manhattan)

print("Running A* with Euclidean Heuristic...")
res_e = a_star(initial, goal, euclidean)

# ===========================
# Results Table
# ===========================

print("\n=== PERFORMANCE COMPARISON ===")
print(f"{'Heuristic':<15} | {'Nodes Explored':<15} | {'Path Length':<12} | {'Time (s)':<10}")
print("-" * 65)

print(f"{'Manhattan':<15} | {res_m['nodes_explored']:<15} | {res_m['path_length']:<12} | {res_m['time']:<10.5f}")
print(f"{'Euclidean':<15} | {res_e['nodes_explored']:<15} | {res_e['path_length']:<12} | {res_e['time']:<10.5f}")



print("\n=== ANALYSIS ===")

if res_m["nodes_explored"] < res_e["nodes_explored"]:
    print("Manhattan explored fewer nodes → More efficient search.")
else:
    print("Euclidean explored fewer nodes → More efficient search.")

if res_m["time"] < res_e["time"]:
    print("Manhattan heuristic ran faster.")
else:
    print("Euclidean heuristic ran faster.")

if res_m["path_length"] == res_e["path_length"]:
    print("Both heuristics found the same optimal path length.")
else:
    print("One heuristic found a shorter solution path (more informed).")
