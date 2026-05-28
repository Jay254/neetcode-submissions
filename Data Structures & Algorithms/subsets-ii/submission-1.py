class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #contain duplicates
        #sort to handle duplicates
        #order doesn't matter, so we use start
        
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(start, path):
            nonlocal res
            res.append(path[:])
            
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res