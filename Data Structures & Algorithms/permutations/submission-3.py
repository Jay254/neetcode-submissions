class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = [False] * n
        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True
                    backtrack(path)
                    path.pop()
                    seen[i] = False

        backtrack([])
        return res