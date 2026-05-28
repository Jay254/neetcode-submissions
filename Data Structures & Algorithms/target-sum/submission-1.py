class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #2 halfs; one of positive numbers, other of negative numbers
        # P - N = target
        # P + N = sum(nums) #all numbers in negs and pos should equal total
        # 2P = target + sum(nums)
        # P = (target + sum(nums)) // 2
        #if target > total or  target < -total impossible
        total = sum(nums)
        if target > total or (target - total) % 2 != 0:
            return 0

        # becomes a coin change II problem
        S = (target + total) // 2 #what we are tryna find, we are trying to come up with this
        dp = [0] * (S+1)
        dp[0] = 1

        for num in nums:
            for x in range(S, num - 1, -1): #but loop backward here becuase we can only use one coin at a time
                dp[x] += dp[x - num]

        return dp[S]