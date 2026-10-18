class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = str(int(''.join(map(str, digits))) + 1)
        return [int(ch) for ch in nums]