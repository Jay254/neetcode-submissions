class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common()[0][0]
        # dic = defaultdict(int)
        # count = (0,0)
        # for num in nums:
        #     dic[num] += 1
        #     cur_max, _ = count
        #     cur_max = max()