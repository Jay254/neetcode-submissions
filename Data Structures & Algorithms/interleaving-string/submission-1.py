class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m+n != o:
            return False

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # we can make empty from both of them being empty

        for i in range(1, m+1): #where s2 is an empty char, so first col
            dp[i][0] = dp[i-1][0] and s1[:i] == s3[:i]

        for j in range(1, n+1): #where s1 is empty, so first row
            dp[0][j] = dp[0][j-1] and s2[:j] == s3[:j]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (
                    (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or 
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                    )#either it matches char from s1 or char from s2

        return dp[m][n]