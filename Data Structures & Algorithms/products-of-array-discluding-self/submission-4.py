class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left_product
        left_p = [1] * len(nums)
        for i in range(1, len(nums)):
            left_p[i] = left_p[i-1] * nums[i-1]
        print(left_p)

        #right_product
        right_p = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right_p[i] = right_p[i+1] * nums[i+1]
        print(right_p)

        return [left_p[i]*right_p[i] for i in range(len(nums))]
