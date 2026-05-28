class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if m[0]<= target <= m[-1]:
                l = 0
                r = len(m) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if m[mid] < target:
                        l = mid + 1
                    elif m[mid] > target:
                        r = mid - 1
                    else:
                        return True

        return False
     