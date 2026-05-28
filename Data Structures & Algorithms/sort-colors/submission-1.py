# import random
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         self.quicksort(nums, 0, len(nums)-1)
        
#     def quicksort(self, nums, low, high):
#         if low < high:
#             pi = self.partition(nums, low, high)
#             self.quicksort(nums, low, pi-1)
#             self.quicksort(nums, pi+1, high)

#     def partition(self, nums, low, high):
#         pi_idx = random.randint(low,high)
#         nums[pi_idx], nums[high] = nums[high], nums[pi_idx]

#         i = low
#         pivot = nums[high]
#         for j in range(low, high):
#             if nums[j] <= pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1

#         nums[i], nums[high] = nums[high], nums[i]

#         return i

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1