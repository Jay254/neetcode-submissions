class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)

        # return max(dp)
        import bisect
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails,num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)