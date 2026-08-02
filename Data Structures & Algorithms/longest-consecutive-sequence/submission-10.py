class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in vals:
                j = num
                count = 0
                while j in vals:
                    count += 1
                    j += 1
                longest = max(longest, count)

        return longest