class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0]:
            return 0

        dp = [[0] * (n) for _ in range(m)]
        dp[0][0] = 1

        for r in range(1, m):
            dp[r][0] = 1 if obstacleGrid[r][0] == 0 and dp[r-1][0] == 1 else 0

        for c in range(1, n):
            dp[0][c] = 1 if obstacleGrid[0][c] == 0 and dp[0][c-1] == 1 else 0

        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]