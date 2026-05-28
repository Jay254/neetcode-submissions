class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = Counter(nums)
        # return counts.most_common()[0][0]
        
        #Boyer-Moore voting algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate