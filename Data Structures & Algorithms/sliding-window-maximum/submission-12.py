class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [max(nums[:k])]
        for i in range(k, len(nums)):
            l = i - k + 1
            res.append(max(nums[l:i+1]))

        return res