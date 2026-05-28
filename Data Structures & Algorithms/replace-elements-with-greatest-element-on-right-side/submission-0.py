class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        res = [-1] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            max_so_far = max(max_so_far, arr[i+1])
            res[i] = max_so_far

        return res