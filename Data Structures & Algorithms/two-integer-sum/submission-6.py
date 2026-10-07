class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if num in dic:
                return [dic[num], i]
            dic[diff] = i

        