class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            mid = (l+r) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr < x:
                l = mid + 1
            else:
                r = mid - 1

        return r