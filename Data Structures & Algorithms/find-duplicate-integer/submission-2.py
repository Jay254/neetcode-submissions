class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # a = set()
        # for num in nums:
        #     if not num in a:
        #         a.add(num)
        #     else:
        #         return num

        #Floyd's cycle detection
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: #they meet (cycle detected)
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        