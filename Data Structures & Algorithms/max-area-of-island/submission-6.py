class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            grid[i][j] = 0
            count = 1
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    count += dfs(nr, nc)

            return count

        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area