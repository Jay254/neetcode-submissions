class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_p = prices[0]

        for price in prices[1:]:
            profit = max(profit, price - prev_p)
            prev_p = min(prev_p, price)

        return profit
