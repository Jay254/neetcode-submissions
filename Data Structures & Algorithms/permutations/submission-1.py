class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #oder doesn't matter -> start from 0

        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(path):
            nonlocal res
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False


        backtrack([])
        return res