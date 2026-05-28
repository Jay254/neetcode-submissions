class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def backtrack(remainder, start, path):
            nonlocal res
            if remainder == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if remainder - nums[i] >= 0:
                    path.append(nums[i])
                    backtrack(remainder-nums[i], i, path)
                    path.pop()



        backtrack(target, 0, [])
        return res