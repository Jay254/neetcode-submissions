class Solution:
    def jump(self, nums: List[int]) -> int:
        # farthest = 0
        # cur_end = 0
        # jump = 0

        # for i in range(len(nums)-1):
        #     farthest = max(farthest,i+nums[i])
        #     if i == cur_end:
        #         jump += 1
        #         cur_end = farthest

        # return jump

        #NEETCODE
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps += 1

        return jumps