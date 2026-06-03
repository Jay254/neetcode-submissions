class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_finish(speed):
            t = 0
            for pile in piles:
                t += math.ceil(pile/speed)

            return t <= h

        while l < r:

            mid = (l + r) //  2

            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return l
