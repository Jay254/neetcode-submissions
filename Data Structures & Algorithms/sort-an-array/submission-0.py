class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        l = r = 0
        arr = []
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])
                r += 1

        arr.extend(left[l:])
        arr.extend(right[r:])

        return arr