class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0

        def dfs(i, xor):
            nonlocal tot
            
            if i == len(nums):
                tot += xor
                return

            dfs(i+1, xor)
            dfs(i+1, xor ^ nums[i])

        dfs(0, 0)

        return tot
