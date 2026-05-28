class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #any order, always start from 0
        #unique - sort elements to track duplicates
        res = []
        n = len(nums)
        nums.sort()
        seen = [False] * n

        def backtrack(path):
            nonlocal res
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if not seen[i]:
                    if i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                        continue
                    seen[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    seen[i] = False


        backtrack([])
        
        return res