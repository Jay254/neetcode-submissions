class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        count = 0
        sums = defaultdict(int)
        sums[0] = 1

        for num in nums:
            pref_sum += num
            if pref_sum - k in sums:
                count += sums[pref_sum-k]
            sums[pref_sum] += 1

        return count