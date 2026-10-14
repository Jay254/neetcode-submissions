class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while heap and len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            if s1 == s2:
                continue
            else:
                heapq.heappush(heap, s2-s1)

        return -heap[0] if heap else 0