class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [0] + [float('inf')] * amount
        print(dp)

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1