class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(query, idx) for idx, query in enumerate(queries)])

        heap = []
        res = [0] * len(queries)
        i = 0

        for query, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(heap, (length, end))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
                
            res[idx] = heap[0][0] if heap else -1


        return res

