class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c):
            
            area = 1
            grid[r][c] = 0
            for dx,dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    area += dfs(nx,ny)

            return area
        
        total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    total = max(total, dfs(r,c))

        return total