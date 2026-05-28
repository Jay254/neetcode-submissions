class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set()
        for num in nums:
            if not num in a:
                a.add(num)
            else:
                return num