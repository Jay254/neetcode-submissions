class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)

        while len(self.heap) > 2:
            s1 = heapq.heappop(self.heap)
            s2 = heapq.heappop(self.heap)

            heapq.heappush(self.heap, s1-s2)

        return -(self.heap[0] - self.heap[1])