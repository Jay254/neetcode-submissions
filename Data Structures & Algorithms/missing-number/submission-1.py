class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # `n` should be the length of the list, not the last element
        total = (n * (n + 1)) // 2  # Sum of numbers from 0 to n
        return total - sum(nums)  # The missing number is the difference
