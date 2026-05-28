class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        #for any day there's 3 possibilities:
        #1. Holding a stock -> either you bought it today, or not selling what yu had yesterday
        #2. Selling a stock -> either holding it yesterday, 
        #3. Rest -> not buying/selling/holding

        hold = -prices[0] #you bought it on day 1, max profit is neg that value
        sold = 0 #ot selling anything on the first day
        rest = 0 #no gain resting

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)