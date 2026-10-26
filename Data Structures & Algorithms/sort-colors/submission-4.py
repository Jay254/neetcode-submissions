import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #quicksort algorithm
        # def quicksort(left, right):
        #     if left >= right:
        #         return 

        #     pivot_idx = partition(left, right)

        #     quicksort(left, pivot_idx-1)
        #     quicksort(pivot_idx+1, right)

        # def partition(left, right):
        #     pivot = random.randint(left, right)
        #     nums[right], nums[pivot] = nums[pivot], nums[right]

        #     pointer = left

        #     for i in range(left, right):
        #         if nums[i] <= nums[right]:
        #             nums[pointer], nums[i] = nums[i], nums[pointer]
        #             pointer += 1

        #     nums[pointer], nums[right] = nums[right], nums[pointer]
        #     return pointer


        # quicksort(0, len(nums)-1)

        #mergesort
        def mergesort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            l = r = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            res.extend(left[l:])
            res.extend(right[r:])

            return res

        nums[:] = mergesort(nums)







