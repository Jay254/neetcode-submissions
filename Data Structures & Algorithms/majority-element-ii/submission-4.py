class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # #O(n) space
        # counts = Counter(nums).most_common()
        # needed = len(nums) / 3
        # res = []

        # for k,v in counts:
        #     if v > needed:
        #         res.append(k)

        # return res
        #Boyer-Moore voting algorithm
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num ==  candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for c in (candidate1, candidate2):
            if c is not None and nums.count(c) > (len(nums) / 3):
                res.append(c)

        return res
