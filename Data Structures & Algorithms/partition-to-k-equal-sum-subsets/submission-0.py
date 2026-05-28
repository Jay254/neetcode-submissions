class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        subs = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return len(set(subs)) == 1

            for i in range(k):
                if subs[i] + nums[idx] <= target:
                    subs[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    subs[i] -= nums[idx]

                if subs[i] == 0:
                    break

            return False

        return backtrack(0)
        