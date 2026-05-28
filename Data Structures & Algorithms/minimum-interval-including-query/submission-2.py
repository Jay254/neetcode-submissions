class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        #sort queries but keep intervals
        sorted_queries = sorted([(q,i) for i,q in enumerate(queries)])

        #variables
        res = [-1] * len(queries)
        j = 0
        heap = []

        for q,i in sorted_queries:

            while j < len(intervals) and intervals[j][0] <= q:
                s, e = intervals[j]
                l = e - s + 1
                heapq.heappush(heap, (l, e))
                j += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[i] = heap[0][0]

        return res

