class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # #brute force
        # res = [max(nums[:k])]
        # for i in range(k, len(nums)):
        #     l = i - k + 1
        #     res.append(max(nums[l:i+1]))

        # return res

        #monotonic deque
        q = deque() #indices, vals in decreasing order
        res = []

        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.popleft()

            if r - l + 1 == k:
                l += 1
                res.append(nums[q[0]])

        return res


