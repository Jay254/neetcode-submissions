class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #wanna have 2 piles, each targeting sum of stones / 2
        # we minus the difference, that's smallest possible weight
        stones_sum = sum(stones)
        target = math.ceil(stones_sum / 2)

        def dfs(i, total):
            if i == len(stones) or total >= target:
                return abs(total - (stones_sum - total)) #first pile - second pile
            if (i, total) in dp:
                return dp[(i, total)]
            #we either include this element, or we skip it
            dp[(i, total)] = min(
                dfs(i+1, total + stones[i]), #we include it in sum total
                dfs(i+1, total) #we don't include it in sum
            )
            return dp[(i, total)]

        dp = {} #hash set
        return dfs(0, 0) # passing index 0 and total which is zero at the beginning
