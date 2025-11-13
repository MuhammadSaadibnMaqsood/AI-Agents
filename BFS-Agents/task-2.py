import time
import random
from collections import deque

def bfs_robot_navigation(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
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


def generate_grid(size, obstacle_density):
    grid = [["." for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_density:
                grid[i][j] = "X"

    grid[0][0] = "S"
    grid[size - 1][size - 1] = "G"
    return grid


start = (0, 0)
goal = (9, 9)

sparse_grid = generate_grid(10, 0.2)
start_time = time.time()
bfs_robot_navigation(sparse_grid, start, goal)
print("Sparse Grid Time:", time.time() - start_time)


dense_grid = generate_grid(10, 0.5)
start_time = time.time()
bfs_robot_navigation(dense_grid, start, goal)
print("Dense Grid Time:", time.time() - start_time)
