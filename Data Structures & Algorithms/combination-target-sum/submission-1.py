class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(n,start, path):
            nonlocal res
            if n == 0:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                if n - nums[i] >= 0:
                    path.append(nums[i])
                    backtrack(n-nums[i], i, path)
                    path.pop()

        backtrack(target,0, [])

        return res