class Solution:
    def maxDifference(self, s: str) -> int:
        s_count = Counter(s)
        max_odd, min_even = float('-inf'), float('inf')

        for cnt in s_count.values():
            if cnt % 2 == 0:
                min_even = min(min_even, cnt)
            else:
                max_odd = max(max_odd, cnt)

        return max_odd - min_even