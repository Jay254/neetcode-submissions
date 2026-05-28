class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDig = ''.join(str(dig) for dig in digits)
        num = int(strDig) + 1
        return list(str(num))