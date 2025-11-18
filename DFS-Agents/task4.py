

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


    
warehouse = [
    ['S', '.', '.', 'X', 'G'], 
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', '.'], 
    ['X', '.', '.', '.', '.'], 
    ['.', '.', 'X', '.', '.']
]

start = (0, 0)
goal = (0, 4)
path = dfs(warehouse, start, goal) 
print("DFS Solution Path:", path)
