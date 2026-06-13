class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)
        while len(self.heap) >= 2:
            s1 = -heapq.heappop(self.heap)
            s2 = -heapq.heappop(self.heap)

            if s1 > s2:
                heapq.heappush(self.heap, -(s1-s2))

        
        return -self.heap[0] if self.heap else 0