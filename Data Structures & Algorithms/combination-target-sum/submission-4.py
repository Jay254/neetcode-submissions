class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def traverse(start, path, remainder):
            nonlocal res
            if remainder == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if remainder - nums[i] >= 0:
                    path.append(nums[i])
                    traverse(i, path, remainder - nums[i])
                    path.pop()

        traverse(0, [], target)
        return res