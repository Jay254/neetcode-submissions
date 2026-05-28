class Solution:
    def dfs(self, grid, i, j):
        # Check for out-of-bounds or water cell
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        
        # Mark the cell as visited by changing '1' to '0'
        grid[i][j] = 0
        
        # Initialize area count for the current island
        area = 1
        
        # Explore all four directions and accumulate the area
        area += self.dfs(grid, i + 1, j)  # Down
        area += self.dfs(grid, i - 1, j)  # Up
        area += self.dfs(grid, i, j + 1)  # Right
        area += self.dfs(grid, i, j - 1)  # Left
        
        return area  # Return the total area of this island

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0  # Initialize max area to zero

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # If it's land
                    # Call dfs to get the area of the island
                    current_area = self.dfs(grid, i, j)
                    # Update max area if the current island is larger
                    max_area = max(max_area, current_area)

        return max_area  # Return the maximum area found