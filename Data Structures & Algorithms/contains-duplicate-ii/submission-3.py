class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len(nums) <= 1:
        #     return False

        # for i in range(len(nums)):
        #     nums[i] = (nums[i], i)
        # nums.sort()

        # for i in range(1, len(nums)):
        #     prev_num, prev_i = nums[i-1]
        #     cur_num, cur_i = nums[i]
        #     if prev_num == cur_num and abs(prev_i - cur_i) <= k:
        #         return True

        # return False

        #sliding window hash set
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False
