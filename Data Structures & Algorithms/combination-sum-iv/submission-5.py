class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # res = []

        # def backtrack(n, arr):
        #     nonlocal res
        #     if n == 0:
        #         res.append(arr[:])
        #     for num in nums:
        #         if n - num >= 0:
        #             arr.append(num)
        #             backtrack(n-num, arr)
        #             arr.pop()


        # backtrack(target,[])

        # return len(res)
        memo = {}

        def dfs(n):
            if n == 0:
                return 1
            if n in memo:
                return memo[n]

            count = 0
            for num in nums:
                if n - num >= 0:
                    count += dfs(n-num)

            memo[n] = count
            return count

        return dfs(target)