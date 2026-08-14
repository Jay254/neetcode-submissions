class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def traverse(path):
            nonlocal res
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                path.append(nums[i])
                traverse(path)
                path.pop()
                seen.remove(nums[i])
                
        traverse([])
        return res
        