class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common(k) # returns [(num, frequency)....]
        return [num for num, freq in counts]