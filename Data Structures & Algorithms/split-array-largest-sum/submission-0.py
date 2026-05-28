class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def can_split(limit):
            cur_sum, count = 0, 1
            for num in nums:
                if cur_sum + num > limit:
                    count += 1
                    cur_sum = num
                else:
                    cur_sum += num
            return count <= k
                

        while l < r:
            mid = (l+r) // 2
            if can_split(mid):
                r = mid
            else:
                l = mid + 1

        return l