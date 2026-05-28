class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_l = 0

        for num in nums:
            if num-1 not in nums_set:
                l = 1
                cur = num
                while cur+1 in nums_set:
                    l += 1
                    cur += 1
                max_l = max(max_l, l)

        return max_l