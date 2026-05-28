class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= k:
            return [max(nums)]
        res = []
        left = 0

        for right in range(k, n+1):
            max_so_far = max(nums[left:right])
            res.append(max_so_far)
            left += 1

        return res
