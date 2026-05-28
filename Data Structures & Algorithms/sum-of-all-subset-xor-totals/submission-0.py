class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def backtrack(start, path):
            # Add the current subset (copy!)
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        # Start the backtracking from index 0 with empty subset
        backtrack(0, [])

        # XOR each subset
        total = 0
        for subset in res:
            xor_val = 0
            for val in subset:
                xor_val ^= val
            total += xor_val

        return total