class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max_p
            max_p = max(num, num * max_p, num * min_p)
            min_p = min(num, num * temp_max, num * min_p)
            res = max(res, max_p)

        return res