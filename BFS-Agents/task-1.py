from collections import deque

def bfs_robot_navigation(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "X" and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None

warehouse = [
    ["S", ".", ".", "X", "G"],
    [".", "X", ".", ".", "."],
    [".", ".", ".", "X", "."],
    ["X", ".", ".", ".", "."],
    [".", ".", "X", ".", "."]
]

start = (0, 0)
goal = (0, 4)

path = bfs_robot_navigation(warehouse, start, goal)
print("\nShortest Path:", path)
