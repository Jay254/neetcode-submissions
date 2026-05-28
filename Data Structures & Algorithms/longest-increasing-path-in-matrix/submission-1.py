class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        #dp for memoization
        dp = [[0] * n for _ in range(m)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c):
            if dp[r][c] != 0:
                return dp[r][c]

            best = 1
            for dx, dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[r][c]:
                    best = max(best, 1 + dfs(nx,ny))

            dp[r][c] = best
            return best
        longest = 0
        for r in range(m):
            for c in range(n):
                longest = max(longest, dfs(r,c))

        return longest