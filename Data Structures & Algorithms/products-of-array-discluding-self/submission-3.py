class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left product
        left_p = [1] * len(nums)
        for i in range(1, len(nums)):
            left_p[i] = left_p[i-1] * nums[i-1]
        #print(left_p)
        # for j in range(len(nums)-2, 0, -1):
        #     left_p[j] = left_p[j] * nums[j+1]
        # print(left_p)
        right_p = [1] * len(nums)
        for j in range(len(nums)-2, -1, -1):
            right_p[j]= nums[j+1] * right_p[j+1]
        print(right_p)

        for k in range(len(nums)):
            left_p[k] = left_p[k] * right_p[k]

        return left_p