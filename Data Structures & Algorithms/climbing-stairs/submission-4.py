class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2 # ways for 2 stairs ago, ways for 1 stair ago

        for _ in range(3, n+1):
            prev2, prev1 = prev1, prev2 + prev1
        
        return prev1