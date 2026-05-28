class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative to simulate max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # Convert list into a heap
        
        # Continue smashing stones until there's one or no stone left
        while len(max_heap) > 1:
            # Extract the two largest stones (most negative values)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            
            # If the stones are not equal, push the remaining weight back into the heap
            if stone1 != stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))
        
        # If there's a stone left, return its weight; otherwise, return 0
        return -max_heap[0] if max_heap else 0