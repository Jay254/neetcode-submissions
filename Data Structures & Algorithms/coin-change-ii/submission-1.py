class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for c in coins: #we are having combinations not permutations
            for x in range(c, amount+1):
                dp[x] += dp[x-c]

        return dp[amount]