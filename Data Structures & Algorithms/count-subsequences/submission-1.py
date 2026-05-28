class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #all char of t should exist in s, which means if t is longer than s, then impossible
        if len(t) > len(s):
            return 0

        def dfs(i,j):
            #if we've reached end of t, means we've matched it completely:
            if j == len(t):
                return 1 #a possible way
            if i == len(s): #reached end of s, we can't make it
                return 0

            #you have two options, skip it, or if they match use it
            res = dfs(i+1,j) #skip this char of s
            if s[i] == t[j]:#skip both since they match
                res += dfs(i+1,j+1)
            return res

        return dfs(0,0) #start indices at both strings