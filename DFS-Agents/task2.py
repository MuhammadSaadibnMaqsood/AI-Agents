import time

def dfs(grid, start, goal):
    visited = set()
    parent_map = {}
    stack = [start]

    row, col = len(grid), len(grid[0])

    while stack:
        current = stack.pop()

        if current == goal:
            path = []
            while current in parent_map:
                path.append(current)
                current = parent_map[current]
            path.append(start)
            return path[::-1]

        if current not in visited:
            visited.add(current)
            x, y = current

            moves = [(0,1), (1,0), (0,-1), (-1,0)]

            for (dx, dy) in moves:
                nx, ny = x + dx, y + dy

                # correct bound checking + obstacle checking
                if 0 <= nx < row and 0 <= ny < col:
                    if grid[nx][ny] != "X" and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        parent_map[(nx, ny)] = current

    return None


def compare_DFS(grid1, grid2, start, goal):

    print("\n--- Sparse Grid DFS ---")
    s1 = time.time()
    path1 = dfs(grid1, start, goal)
    e1 = time.time()
    print("Path:", path1)
    print("Execution Time:", e1 - s1, "seconds")

    print("\n--- Dense Grid DFS ---")
    s2 = time.time()
    path2 = dfs(grid2, start, goal)
    e2 = time.time()
    print("Path:", path2)
    print("Execution Time:", e2 - s2, "seconds")


# Grids
sparse_grid = [
    ['S', '.', '.', 'X', 'G'], 
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', '.'], 
    ['X', '.', '.', '.', '.'], 
    ['.', '.', 'X', '.', '.']
]

dense_grid = [ 
    ['S', 'X', 'X', 'X', 'G'], 
    ['X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X']
]


start = (0, 0)
goal = (0, 4)

compare_DFS(sparse_grid, dense_grid, start, goal)
