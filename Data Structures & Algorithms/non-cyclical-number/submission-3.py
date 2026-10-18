class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = sum(int(dig) ** 2 for dig in str(n))
            if n in seen:
                return False
            seen.add(n)

        return True