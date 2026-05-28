class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        #sort
        nums.sort()
        #[-4,-1,-1,0,1,2]

        for i, num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1

            while l < r:
                sum = num + nums[l] + nums[r]

                if sum < 0:
                    l = l + 1
                elif sum > 0:
                    r = r - 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l = l + 1

                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1

        return res


        