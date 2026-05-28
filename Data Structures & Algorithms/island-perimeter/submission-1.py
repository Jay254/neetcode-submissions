class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    neighbors = 4
                    for dx, dy in directions:
                        nx, ny = dx+r, dy+c
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                            neighbors -= 1
                    per += neighbors


        return per

        
