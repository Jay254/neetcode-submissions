class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        sub = total // k
        subs = [0] * k
        nums.sort(reverse=True)

        def backtrack(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if nums[idx] + subs[i] <= sub:
                    subs[i] += nums[idx]

                    if backtrack(idx+1):
                        return True

                    subs[i] -= nums[idx]

                if subs[i] == 0:
                    return False

            return False

        return backtrack(0)