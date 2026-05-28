class Solution:
    def integerBreak(self, n: int) -> int:
        # #brute force backtracking
        # best = 0
        # def backtrack(remaining, path):
        #     nonlocal best
        #     if remaining == 0:
        #         prod = 1
        #         for num in path:
        #             prod *= num
        #         best = max(prod, best)
        #         return
        #     for i in range(1, remaining+1):
        #         if sum(path) + i < n:
        #             path.append(i)
        #             backtrack(remaining-i, path)
        #             path.pop()

        # backtrack(n, [])
        # return best

        #backtracking with memo
        memo = {}
        def backtrack(remaining):
            if remaining == 0:
                return 1
            if remaining in memo:
                return memo[remaining]
            
            best = 0
            for i in range(1, remaining):
                no_break = i * (remaining-i)
                with_break = i * backtrack(remaining-i)
                best = max(best, no_break, with_break)

            memo[remaining] = best
            return best

        backtrack(n)
        return memo[n]