class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                dfs(nx,ny)


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1

        return res