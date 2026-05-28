class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def num_sides(i, j):
            sides = 4
            if 0 <= i-1 < m and grid[i-1][j] == 1:
                sides -= 1
            if 0 <= i+1 < m and grid[i+1][j] == 1:
                sides -= 1
            if 0 <= j+1 < n and grid[i][j+1] == 1:
                sides -= 1
            if 0 <= j-1 < n and grid[i][j-1] == 1:
                sides -= 1
            return sides

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += num_sides(i,j)

        return total