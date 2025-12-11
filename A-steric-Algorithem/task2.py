from heapq import heappop, heappush

# Manhattan Distance Heuristic
def manhattan(state, goal):
    distance = 0
    for i in range(1, 9):       # Tile numbers 1 to 8 (skip 0)
        x1, y1 = divmod(state.index(i), 3)   # Tile i current position
        x2, y2 = divmod(goal.index(i), 3)    # Tile i goal position
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# Generate valid neighbor states
def neighbors(state):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]   # Down, Up, Right, Left
    idx = state.index(0)                          # Location of the empty tile
    x, y = divmod(idx, 3)                         # Convert index → 2D position

    possible_moves = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Check if new position is inside 3x3 grid
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = state[:]                  # copy list
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            possible_moves.append(new_state)

    return possible_moves


# A* Algorithm
def a_star(start, goal):

    open_set = []
    heappush(open_set, (0, start, []))
    visited = set()

    while open_set:
        f, current, path = heappop(open_set)

        if current == goal:
            return path

        visited.add(tuple(current))

        for move in neighbors(current):
            if tuple(move) not in visited:
                new_path = path + [move]
                g = len(new_path)
                h = manhattan(move, goal)
                heappush(open_set, (g + h, move, new_path))

    return None


start_state = [
    
    [1, 2, 3, 4, 0, 5, 6, 7, 8], 
    [1, 2, 3, 5, 0, 6, 4, 7, 8], 
    [5, 1, 3, 4, 2, 8, 7, 0, 6] 
]

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]


for state in start_state:
    solution_path = a_star(state, goal_state)
    print("Solution Path:")
    for step in solution_path:
        print(step)
    


