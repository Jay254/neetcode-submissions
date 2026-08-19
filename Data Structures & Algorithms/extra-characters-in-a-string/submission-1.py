class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #count ch as extra
        #count if word starts there
        memo = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in memo:
                return memo[i]

            #as extra
            res = 1 + dfs(i+1)

            for word in dictionary:
                if s.startswith(word,i):
                    res = min(res, dfs(i+len(word)))

            memo[i] = res
            return res

        return dfs(0)