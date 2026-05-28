class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, cur = 0, 0
        for i in range(2, len(cost)+1):
            cur_cost = min(cost[i-1]+cur, cost[i-2]+prev)
            prev,cur = cur, cur_cost

        return cur