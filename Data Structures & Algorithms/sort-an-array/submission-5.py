class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

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

        return mergeSort(nums)