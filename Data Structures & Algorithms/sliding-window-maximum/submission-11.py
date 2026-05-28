class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # if n <= k:
        #     return [max(nums)]
        # res = []
        # left = 0

        # for right in range(k, n+1):
        #     max_so_far = max(nums[left:right])
        #     res.append(max_so_far)
        #     left += 1

        # return res
        n = len(nums)
        if n == 0:
            return []
        if n <= k:
            return [max(nums)]
    
        dq = deque()
        res = []

        for i in range(n):
            while dq and dq[0] < i - k + 1: #shrinking window
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]: #removing smaller elements from the back
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res