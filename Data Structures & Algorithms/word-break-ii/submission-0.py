class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        wordDict = set(wordDict)

        def backtrack(start, path):
            if start == n:
                res.append(' '.join(path))
                return
            for i in range(start, n):
                substr = s[start:i+1]
                if substr in wordDict:
                    path.append(substr)
                    backtrack(i+1, path)
                    path.pop()




        backtrack(0,[])

        return res
