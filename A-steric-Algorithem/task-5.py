from heapq import heappush, heappop

# -------------------------------------------------------
# Manhattan Distance Heuristic
# -------------------------------------------------------
def manhattan(state, goal):
    distance = 0
    for i in range(1, 16):  # tiles 1 to 15
        x1, y1 = divmod(state.index(i), 4)
        x2, y2 = divmod(goal.index(i), 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# -------------------------------------------------------
# Misplaced Tile Heuristic
# -------------------------------------------------------
def misplaced_tiles(state, goal):
    return sum(1 for i in range(16) if state[i] != 0 and state[i] != goal[i])

# -------------------------------------------------------
# Neighbor Generator for 15 Puzzle
# -------------------------------------------------------
def neighbor(state):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    moves = []

    idx = state.index(0)              # empty tile position
    x, y = divmod(idx, 4)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            new_idx = nx * 4 + ny
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            moves.append(new_state)

    return moves

# -------------------------------------------------------
# A* Search with Node Exploration Count
# -------------------------------------------------------
def a_star_with_heuristic(initial, goal, heuristic):

    visited = set()
    pq = []
    heappush(pq, (0, initial, []))

    explored_nodes = 0

    while pq:
        f, current, path = heappop(pq)
        explored_nodes += 1

        if current == goal:
            return path, explored_nodes

        visited.add(tuple(current))

        for move in neighbor(current):
            if tuple(move) not in visited:
                new_path = path + [move]
                g = len(new_path)
                h = heuristic(move, goal)
                heappush(pq, (g + h, move, new_path))

    return None, explored_nodes


# -------------------------------------------------------
# Test Initial and Goal States
# -------------------------------------------------------
initial = [
    1,  2,  3,  4,
    5,  6,  7,  8,
    9, 10, 11, 12,
    0, 13, 14, 15
]

goal = [
    1,  2,  3,  4,
    5,  6,  7,  8,
    9, 10, 11, 12,
    13, 14, 15, 0
]

# -------------------------------------------------------
# Run Both Heuristics
# -------------------------------------------------------
man_path, man_nodes = a_star_with_heuristic(initial, goal, manhattan)
mis_path, mis_nodes = a_star_with_heuristic(initial, goal, misplaced_tiles)

# -------------------------------------------------------
# OUTPUT RESULTS
# -------------------------------------------------------
print("\n===== A* Manhattan Heuristic =====")
print("Path Length:", len(man_path))
print("Nodes Explored:", man_nodes)

print("\n===== A* Misplaced Tiles Heuristic =====")
print("Path Length:", len(mis_path))
print("Nodes Explored:", mis_nodes)

print("\n===== Manhattan Search Path =====")
for step in man_path:
    print(step)
