class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = None

        for num in nums:
            if count == 0:
                major = num
                count += 1

            if num == major:
                count += 1

            else:
                count -= 1

        return major