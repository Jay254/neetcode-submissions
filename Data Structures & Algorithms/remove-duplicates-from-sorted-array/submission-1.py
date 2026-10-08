class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        res = []

        for num in nums:
            if num not in seen:
                res.append(num)
            seen.add(num)

        nums[:] = res
        return len(nums)