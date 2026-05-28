class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        i = 1
        squares = []
        while i * i <= n:
            squares.append(i*i)
            i += 1

        for square in squares:
            for i in range(square, n+1):
                dp[i] = min(dp[i], dp[i-square]+1)

        return dp[n]