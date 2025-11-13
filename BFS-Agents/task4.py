from collections import deque

def chocolate_factory_shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) 

    moves = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0)   # up
    ]

    queue = deque([(start, [start])])  
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path  

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if (0 <= nx < rows and 0 <= ny < cols and 
                    grid[nx][ny] != "X" and               
                    (nx, ny) not in visited):             
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None 

factory = [
    ["S", ".", ".", "X", "G"],
    [".", "X", ".", ".", "."],
    [".", ".", ".", "X", "."],
    ["X", ".", ".", ".", "."],
    [".", ".", "X", ".", "."]
]

start = (0, 0)
goal = (0, 4)

path = chocolate_factory_shortest_path(factory, start, goal)
print("Shortest Path:", path)
