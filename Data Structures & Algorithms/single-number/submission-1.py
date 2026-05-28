class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # for val in counter:
        #     if counter[val] == 1:
        #         return val
        #NEETCODE -> XOR
        res = 0
        for num in nums:
            res ^= num
        return res