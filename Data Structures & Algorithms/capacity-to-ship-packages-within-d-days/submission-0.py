class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        l, r = max(weights), total

        def can_carry(w):
            days_used = 1
            cur_load = 0
            for weight in weights:
                if cur_load + weight > w:
                    days_used += 1
                    cur_load = 0
                cur_load += weight

            return days_used <= days

        while l <= r:
            w = (l+r) // 2
            if can_carry(w):
                r = w-1
            else:
                l = w + 1

        return l