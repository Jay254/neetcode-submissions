class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for start, end in intervals:
            if res and start <= res[-1][1]:
                s, e = res.pop()
                start = min(start, s)
                end = max(end, e)

            res.append([start, end])

        return res