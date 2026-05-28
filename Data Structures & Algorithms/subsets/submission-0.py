class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, current):
            # Add the current subset to the result
            result.append(current[:])

            # Explore options to include more numbers in the subset
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                current.append(nums[i])
                # Recurse with the current subset
                backtrack(i + 1, current)
                # Backtrack: remove the last added number
                current.pop()

        result = []
        backtrack(0, [])
        return result