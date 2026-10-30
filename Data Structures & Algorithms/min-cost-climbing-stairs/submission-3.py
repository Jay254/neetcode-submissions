class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0 #cost to reach 2 steps ago, cost to reach 1 step ago

        for i in range(2, len(cost)+1):
            cur = min(
                prev2 + cost[i-2],
                prev1 + cost[i-1]
            )
            prev2 = prev1
            prev1 = cur

        return prev1