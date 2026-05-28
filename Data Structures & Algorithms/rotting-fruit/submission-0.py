class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        
        # Collect all initially rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges at the start, return 0
        if fresh_oranges == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        # BFS
        while queue:
            level_size = len(queue)
            made_progress = False
            for _ in range(level_size):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check if the new cell is within bounds and is a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot this orange
                        fresh_oranges -= 1
                        queue.append((nx, ny))
                        made_progress = True

            # Only increment time if some oranges rotted in this minute
            if made_progress:
                time += 1

        # If there are still fresh oranges left, return -1
        return time if fresh_oranges == 0 else -1