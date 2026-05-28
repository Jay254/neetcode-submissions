class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        
        # Step 1: Add all treasure chests (0s) to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Perform BFS from all treasure chests
        while queue:
            x, y = queue.popleft()
            
            # Explore neighbors in 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the neighbor is a valid land cell
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1  # Update distance
                    queue.append((nx, ny))  # Add to queue for further exploration