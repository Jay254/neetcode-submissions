class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1

        prev3, prev2, prev1 = 0, 1, 1

        for _ in range(3, n+1):
            cur = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = cur

        return prev1