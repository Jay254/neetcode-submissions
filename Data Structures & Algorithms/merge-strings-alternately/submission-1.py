class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        loop = min(len(word1), len(word2))
        res = ''
        for i in range(loop):
            res += word1[l] + word2[r]
            l += 1
            r += 1

        res += word1[loop:] + word2[loop:]

        return res

        

        
