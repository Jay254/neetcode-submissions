class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def robb(arr):
            n = len(arr)
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1] = arr[0]
            for i in range(2,n+1):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i-1])

            return dp[n]


        option1 = robb(nums[1:])
        option2 = robb(nums[:-1])

        return max(option1,option2)