class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_finish(speed):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/speed)
                if hrs > h:
                    return False
            return True

        while l <= r:
            speed = (l + r) // 2
            if can_finish(speed):
                r = speed - 1
            else:
                l = speed + 1

        return l