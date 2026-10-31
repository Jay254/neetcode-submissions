class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            for dr, dc in directions:
                nr, nc = dr+i, dc+j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count