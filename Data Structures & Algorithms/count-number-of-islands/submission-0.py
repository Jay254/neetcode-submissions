class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        # Check boundaries and if the current cell is water or already visited
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        # Mark the cell as visited by changing '1' to '0'
        grid[i][j] = '0'
        
        # Visit all adjacent cells (up, down, left, right)
        self.dfs(grid, i + 1, j)  # Down
        self.dfs(grid, i - 1, j)  # Up
        self.dfs(grid, i, j + 1)  # Right
        self.dfs(grid, i, j - 1)  # Left

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If we find an unvisited land cell
                if grid[i][j] == '1':
                    count += 1  # Increment island count
                    self.dfs(grid, i, j)  # Call DFS to mark the entire island
        
        return count