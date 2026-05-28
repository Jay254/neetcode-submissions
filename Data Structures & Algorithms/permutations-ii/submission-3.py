class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = [False] * len(nums)
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if seen[i]:
                    continue
                else:
                    if i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                        continue
                    else:
                        seen[i] = True
                        path.append(nums[i])
                        backtrack(path)
                        path.pop()
                        seen[i] = False
        backtrack([])
        return res