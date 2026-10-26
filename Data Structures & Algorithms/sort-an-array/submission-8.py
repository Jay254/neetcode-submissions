import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # #mergesort
        # def mergeSort(arr):
        #     if len(arr) <= 1:
        #         return arr

        #     mid = len(arr) // 2

        #     left = mergeSort(arr[:mid])
        #     right = mergeSort(arr[mid:])

        #     return merge(left, right)

        # def merge(left, right):
        #     res = []
        #     l = r = 0

        #     while l < len(left) and r < len(right):
        #         if left[l] <= right[r]:
        #             res.append(left[l])
        #             l += 1
        #         else:
        #             res.append(right[r])
        #             r += 1

        #     res.extend(left[l:])
        #     res.extend(right[r:])

        #     return res

        # return mergeSort(nums)

        #quicksort
        def quicksort(left, right):
            if left >= right:
                return

            pivot_index = partition(left, right)

            quicksort(left, pivot_index-1)
            quicksort(pivot_index+1, right)

        def partition(left, right):
            pivot_pos = random.randint(left, right)
            nums[pivot_pos], nums[right] = nums[right], nums[pivot_pos]

            pivot = nums[right]
            pointer = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1

            nums[pointer], nums[right] = nums[right], nums[pointer]

            return pointer

        quicksort(0, len(nums)-1)

        return nums