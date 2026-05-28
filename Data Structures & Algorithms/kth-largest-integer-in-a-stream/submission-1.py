import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # Convert nums into a heap
        heapq.heapify(self.nums)
        # Keep only the k largest elements in the heap
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.nums, val)
        # If the heap grows larger than k, pop the smallest element
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The root of the heap is the kth largest element
        return self.nums[0]
