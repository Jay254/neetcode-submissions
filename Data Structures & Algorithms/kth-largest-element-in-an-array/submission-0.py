class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap
        min_heap = []
        
        # Iterate over all numbers
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # If the heap exceeds size k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the k-th largest element
        return heapq.heappop(min_heap)