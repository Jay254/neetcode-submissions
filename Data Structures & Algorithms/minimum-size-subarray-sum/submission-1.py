class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float('inf')
        summ = 0

        for right in range(n):
            summ += nums[right]

            while summ >= target:
                min_len = min(min_len, (right-left+1))
                summ -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0