class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_arr = nums1 + nums2
        nums = sorted(nums_arr)

        low, high = 0, len(nums)-1
        mid = math.ceil((low+high) / 2)
        print(low,mid, high)

        if ((len(nums) % 2) == 0):
            print(nums[mid-1], nums[mid])
            return (nums[mid-1] + nums[mid]) / 2
        else:
            return nums[mid]