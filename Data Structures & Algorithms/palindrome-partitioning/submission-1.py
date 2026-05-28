class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        n = len(s)
        def backtrack(start, path):
            nonlocal res
            if start == n:
                res.append(path[:])

            for i in range(start, n):
                substr = s[start:i+1]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(i+1, path)
                    path.pop()


        backtrack(0, [])
        return res