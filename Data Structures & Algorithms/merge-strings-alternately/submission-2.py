class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        loop = min(len(word1), len(word2))
        res = ''
        for i in range(loop):
            res += word1[i] + word2[i]

        return res + word1[loop:] + word2[loop:]

        

        
