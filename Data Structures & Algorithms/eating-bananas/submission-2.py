class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low+high) // 2
            total_hours = 0
            for pile in piles:
                time_taken = math.ceil(pile/mid)
                total_hours += time_taken

            if total_hours <= h:
                high = mid -1
            else:
                low = mid + 1


        return low