class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(remaining, start, path):
            nonlocal res
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if remaining - nums[i] >= 0:
                    path.append(nums[i])
                    backtrack(remaining - nums[i], i, path)
                    path.pop()

        backtrack(target, 0, [])
        return res
