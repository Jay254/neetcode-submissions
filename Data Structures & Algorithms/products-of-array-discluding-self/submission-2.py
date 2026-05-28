class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_p = [1] * n
        for i in range(1, n):
            left_p[i] = left_p[i-1] * nums[i-1] 

        right_p = 1
        for i in range(n-1, -1, -1):
            left_p[i] *= right_p
            right_p *= nums[i]
        
        return left_p