from heapq import heappush, heappop


def manhattan(state, goal):
    distance = 0
    for i in range(1, 16):  # tiles 1 to 15
        x1, y1 = divmod(state.index(i), 4)
        x2, y2 = divmod(goal.index(i), 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def neighbor(state):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
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


def a_star(initial, goal):
    visited = set()
    pq = []

    heappush(pq, (0, initial, []))

    while pq:
        f, current, path = heappop(pq)

        if current == goal:
            return path

        visited.add(tuple(current))

        for move in neighbor(current):
            if tuple(move) not in visited:
                new_path = path + [move]
                g = len(new_path)
                h = manhattan(move, goal)
                heappush(pq, (g + h, move, new_path))

    return None


initial = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    0, 13, 14, 15
]

goal = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 0
]

solution_path = a_star(initial, goal)

print("Solution Path:")
for step in solution_path:
    print(step)
