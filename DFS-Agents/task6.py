def dfs_hidden_gem(capacity1, capacity2, target):

    parent_map = {}
    visited = set()
    stack = [(0, 0)]     # must be LIST of tuples, not a tuple

    while stack:
        flask1, flask2 = stack.pop()

        # Goal found
        if flask1 == target or flask2 == target:
            path = []
            while (flask1, flask2) in parent_map:
                path.append((flask1, flask2))
                flask1, flask2 = parent_map[(flask1, flask2)]
            path.append((0, 0))
            return path[::-1]

        # Visit state
        if (flask1, flask2) not in visited:
            visited.add((flask1, flask2))

            moves = [
                (capacity1, flask2),  # Fill Flask 1
                (flask1, capacity2),  # Fill Flask 2
                (0, flask2),          # Empty Flask 1
                (flask1, 0),          # Empty Flask 2
                # Flask 1 → Flask 2
                (
                    flask1 - min(flask1, capacity2 - flask2),
                    flask2 + min(flask1, capacity2 - flask2)
                ),
                # Flask 2 → Flask 1
                (
                    flask1 + min(flask2, capacity1 - flask1),
                    flask2 - min(flask2, capacity1 - flask1)
                )
            ]

            for move in moves:
                if move not in visited:
                    stack.append(move)
                    parent_map[move] = (flask1, flask2)

    return None

capacity1, capacity2, target = 3, 6, 4
print("\nDFS Solution Path for Hidden Gem Bistro:")
dfs_path = dfs_hidden_gem(capacity1, capacity2, target)
print("\n",dfs_path)
