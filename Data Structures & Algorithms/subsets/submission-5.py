class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(idx, path):
            res.append(path[:])

            for i in range(idx, len(nums)):
                path.append(nums[i])
                traverse(i+1, path)
                path.pop()

        traverse(0, [])
        return res