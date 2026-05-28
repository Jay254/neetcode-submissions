class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # if n < 2:
        #     return [nums[1], nums[0]]
        result = [1] * n

        left_p = 1
        # right_p = [1]
        for i in range(n):
            result[i] = left_p
            left_p *= nums[i]

        right_p = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_p
            right_p *= nums[i]

        return result
            