from collections import deque

def bfs_cafe_oasis(capacity1,capacity2,target):
    visited = set()
    parent_map = {}
    queue = deque([(0,0)])

    while queue:
        
        flask1,flask2 = queue.popleft()

        if flask1 == target or flask2 == target:
            path = []

            while (flask1,flask2) in parent_map:
                path.append((flask1,flask2))
                flask1,flask2 = parent_map[(flask1,flask2)]
            
            path.append((0,0))
            return path[::-1]
        
        if (flask1,flask2) not in visited:
            visited.add((flask1,flask2))

            moves = [
                (capacity1,flask2),
                (flask1,capacity2),
                (0,flask2),
                (flask1,0),
                (flask1 - min(flask1, capacity2 - flask2), flask2 + min(flask1, capacity2 - flask2)),
                (flask1 + min(flask2, capacity1 - flask1), flask2 - min(flask2, capacity1 - flask1))


            ]

            for move in moves:
                if move not in visited:
                    queue.append(move)
                    parent_map[move] = (flask1,flask2)
    return None

capacity1, capacity2, target = 5, 3, 4 
print("BFS Solution Path for Café Oasis:") 
bfs_path = bfs_cafe_oasis(capacity1, capacity2, target) 
print(bfs_path if bfs_path else "No solution found")