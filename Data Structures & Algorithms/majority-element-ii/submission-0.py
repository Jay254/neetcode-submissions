class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums).most_common()
        needed = len(nums) / 3
        res = []

        for k,v in counts:
            if v > needed:
                res.append(k)

        return res
