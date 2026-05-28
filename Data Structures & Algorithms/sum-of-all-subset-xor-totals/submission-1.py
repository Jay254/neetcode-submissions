class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, xor):
            nonlocal res
            if i  == len(nums):
                res += xor
                return 

            #include this val
            backtrack(i+1, xor ^ nums[i])
            #exclude it
            backtrack(i+1, xor)
            
        backtrack(0, 0)

        return res