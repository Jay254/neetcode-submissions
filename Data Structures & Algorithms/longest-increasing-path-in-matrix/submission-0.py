class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)] #down, up, right, left

        def dfs(i,j):
            if dp[i][j] != 0: #path memoization
                return dp[i][j]

            max_len = 1
            for r,c in directions:
                nr, nc = i+r, j+c
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc] > matrix[i][j]:
                    max_len = max(max_len, 1+dfs(nr,nc))

            dp[i][j] = max_len
            return max_len

        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i,j))

        return max_len