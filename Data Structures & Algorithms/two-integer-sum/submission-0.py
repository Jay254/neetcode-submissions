class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if not nums
#         a = dict()
#         for i, j in enumerate(nums):
#             if j in a:
#                 return [a[j],i]
# #{4:0}
#             a[target - j] = i







        j = dict()
        for i in range(len(nums)):
            if nums[i] in j:
                return [j[nums[i]], i]
            else:
                j[target-nums[i]] = i
