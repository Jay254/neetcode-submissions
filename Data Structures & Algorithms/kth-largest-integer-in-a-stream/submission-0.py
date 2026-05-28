class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        sorted_vals = sorted(self.nums, reverse=True)
        return sorted_vals[self.k-1]
        
