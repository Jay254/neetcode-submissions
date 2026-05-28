class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while heap and len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            elif x > y:
                heapq.heappush(heap, -(x-y))

        
        if len(heap) == 1:
            return -heapq.heappop(heap)
        return 0