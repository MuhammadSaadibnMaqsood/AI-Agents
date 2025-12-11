from heapq import heappop, heappush
from collections import deque

def manhattan(state, goal):
    distance = 0
    for i in range(1, 9):  # tiles 1–8 (ignore 0)
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance



def misplaced_tiles(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])



def neighbors(state):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]   # down, up, right, left
    
    idx = state.index(0)
    x, y = divmod(idx, 3)
    
    possible_moves = []
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            possible_moves.append(new_state)
    
    return possible_moves



def a_star_with_heuristic(start, goal, heuristic):

    open_set = []
    heappush(open_set, (0, start, []))  # (f, state, path)

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
                h = heuristic(move, goal)
                heappush(open_set, (g + h, move, new_path))
    
    return None



def get_neighbors(pos, grid):
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    x, y = pos
    rows, cols = len(grid), len(grid[0])
    
    valid = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "X":
            valid.append((nx, ny))
    
    return valid


def bfs(start, goal, grid):

    queue = deque([start])
    visited = set([start])
    steps = 0

    while queue:

        pos = queue.popleft()

        if pos == goal:
            return steps, len(visited)

        for neigh in get_neighbors(pos, grid):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)

        steps += 1

    return None


def dfs(start, goal, grid):
    
    stack = [start]
    visited = set([start])
    steps = 0

    while stack:

        pos = stack.pop()

        if pos == goal:
            return steps, len(visited)

        for neigh in get_neighbors(pos, grid):
            if neigh not in visited:
                visited.add(neigh)
                stack.append(neigh)

        steps += 1

    return None



start_state = [1,2,3,4,0,5,6,7,8]

goal_state = [1,2,3,4,5,6,7,8,0]

print("\n===== A* USING MANHATTAN DISTANCE =====")
manhattan_path = a_star_with_heuristic(start_state, goal_state, manhattan)
print("Steps:", len(manhattan_path))
for step in manhattan_path:
    print(step)

print("\n===== A* USING MISPLACED TILES =====")
misplaced_path = a_star_with_heuristic(start_state, goal_state, misplaced_tiles)
print("Steps:", len(misplaced_path))
for step in misplaced_path:
    print(step)



warehouse_grid = [
    [".",".",".","."],
    [".","X",".","."],
    [".",".",".","."],
    [".",".","X","."]
]

start_position = (0,0)
goal_position  = (3,3)

bfs_steps, bfs_visited = bfs(start_position, goal_position, warehouse_grid)
dfs_steps, dfs_visited = dfs(start_position, goal_position, warehouse_grid)

print("\n===== GRID SEARCH COMPARISON =====")
print("BFS Steps:", bfs_steps, "Visited:", bfs_visited)
print("DFS Steps:", dfs_steps, "Visited:", dfs_visited)
