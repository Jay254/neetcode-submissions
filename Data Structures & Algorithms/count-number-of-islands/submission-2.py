class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count  = 0

        def dfs(r,c):

            grid[r][c] = '0'

            for dx, dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(nx,ny)


        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count