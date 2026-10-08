class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = set()
        # res = []

        # for num in nums:
        #     if num not in seen:
        #         res.append(num)
        #     seen.add(num)

        # nums[:] = res
        # return len(nums)
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k