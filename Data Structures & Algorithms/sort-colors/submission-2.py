import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #quicksort algorithm
        def quicksort(left, right):
            if left >= right:
                return 

            pivot_idx = partition(left, right)

            quicksort(left, pivot_idx-1)
            quicksort(pivot_idx+1, right)

        def partition(left, right):
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]

            pointer = left

            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1

            nums[pointer], nums[right] = nums[right], nums[pointer]
            return pointer


        quicksort(0, len(nums)-1)