import collections
import heapq
 
def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando BFS."""
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
                if cell != 1 and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    new_path = list(path)
                    new_path.append((next_row, next_col))
                    queue.append(((next_row, next_col), new_path))
 
    return None, 0
 
 
def solve_maze_dfs(maze, start, end):
    """Resuelve el laberinto usando DFS."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()
    visited.add(start)
 
    while stack:
        (curr_row, curr_col), path = stack.pop()
 
        if (curr_row, curr_col) == end:
            return path, len(path)
 
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
 
            if 0 <= next_row < rows and 0 <= next_col < cols:
                cell = maze[next_row][next_col]
                if cell != 1 and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    new_path = list(path)
                    new_path.append((next_row, next_col))
                    stack.append(((next_row, next_col), new_path))
 
    return None, 0
 
 
def heuristic(a, b):
    """Distancia Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
 
def solve_maze_astar(maze, start, end):
    """Resuelve el laberinto usando A*."""
    rows, cols = len(maze), len(maze[0])
    # (f_cost, g_cost, nodo, path)
    heap = [(heuristic(start, end), 0, start, [start])]
    visited = set()
 
    while heap:
        f, g, (curr_row, curr_col), path = heapq.heappop(heap)
 
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
 
        if (curr_row, curr_col) == end:
            return path, len(path)
 
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
 
            if 0 <= next_row < rows and 0 <= next_col < cols:
                cell = maze[next_row][next_col]
                if cell != 1 and (next_row, next_col) not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic((next_row, next_col), end)
                    new_path = list(path)
                    new_path.append((next_row, next_col))
                    heapq.heappush(heap, (new_f, new_g, (next_row, next_col), new_path))
 
    return None, 0
