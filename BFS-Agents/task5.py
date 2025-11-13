import random
import time
from collections import deque

def generate_grid(size, obstacle_density):
    grid = [["." for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_density:
                grid[i][j] = "X"  

    grid[0][0] = "S"                 
    grid[size - 1][size - 1] = "G"   
    return grid


def bfs_robot_navigation(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])  
    visited = set([start])
    moves = [(0,1), (1,0), (0,-1), (-1,0)] 

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "X" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None 

size = 10
start = (0, 0)
goal = (size - 1, size - 1)

densities = {
    "Low (20%)": 0.2,
    "Medium (40%)": 0.4,
    "High (60%)": 0.6
}

for label, density in densities.items():
    grid = generate_grid(size, density)

    start_time = time.time()
    path = bfs_robot_navigation(grid, start, goal)
    exec_time = time.time() - start_time

    print(f"\nGrid Type: {label}")
    print("Execution Time:", round(exec_time, 4), "seconds")

    if path:
        print("Path Length:", len(path))
    else:
        print("No path found (too many obstacles).")
