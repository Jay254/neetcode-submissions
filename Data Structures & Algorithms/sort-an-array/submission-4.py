import random
class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums) <= 1:
    #         return nums
    #     mid = len(nums) // 2
    #     left = self.sortArray(nums[:mid])
    #     right = self.sortArray(nums[mid:])

    #     return self.merge(left, right)

    # def merge(self, left, right):
    #     l = r = 0
    #     arr = []
        
    #     while l < len(left) and r < len(right):
    #         if left[l] <= right[r]:
    #             arr.append(left[l])
    #             l += 1
    #         else:
    #             arr.append(right[r])
    #             r += 1

    #     arr.extend(left[l:])
    #     arr.extend(right[r:])

    #     return arr
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, low, high):
        if low < high:
            p = self.partition(nums, low, high)
            self.quicksort(nums, low, p - 1)
            self.quicksort(nums, p + 1, high)

    def partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)
        nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i