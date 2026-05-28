class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(' '.join(path))
                return

            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    path.append(s[start:i+1])
                    backtrack(i+1, path)
                    path.pop()

        backtrack(0, [])

        return res