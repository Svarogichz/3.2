import collections

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando BFS. Trata 2 y 3 como celdas transitables."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path, len(path)

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols:
                cell = maze[next_row][next_col]
                # Transitable si no es muro (1)
                if cell != 1 and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    new_path = list(path)
                    new_path.append((next_row, next_col))
                    queue.append(((next_row, next_col), new_path))

    return None, 0
