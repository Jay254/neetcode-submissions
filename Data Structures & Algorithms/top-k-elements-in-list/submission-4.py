class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common()
        res = []
        for i in range(k):
            k, v = counts[i]
            res.append(k)

        return res