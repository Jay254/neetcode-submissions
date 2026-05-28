class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return 0

            if (l,r) in dp: #memoize it
                return dp[(l,r)]

            best = 0
            for i in range(l, r+1):
                coins = dfs(l, i-1) + (nums[l-1] * nums[i] * nums[r+1]) + dfs(i+1,r)
                best = max(best, coins)
            
            dp[(l,r)] = best
            return best

        nums = [1] + nums + [1]
        dp = {}
        return dfs(1,len(nums)-2)