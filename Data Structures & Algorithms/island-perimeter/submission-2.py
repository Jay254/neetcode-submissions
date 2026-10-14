class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        per = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                #top
                if r == 0 or grid[r-1][c] == 0:
                    per += 1
                
                #down
                if r == m-1 or grid[r+1][c] == 0:
                    per += 1

                #left
                if c == 0 or grid[r][c-1] == 0:
                    per += 1

                #right
                if c == n-1 or grid[r][c+1] == 0:
                    per += 1

        return per