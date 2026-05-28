class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            cur = best = nums[0]
            for num in nums[1:]:
                cur = max(num, cur+num)
                best = max(best, cur)

            return best

        total = sum(nums)
        max_normal = kadane(nums)
        min_sub = -kadane([-x for x in nums])

        if max_normal < 0:
            return max_normal

        return max(max_normal, total - min_sub)