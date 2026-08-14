class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def traverse(idx, path):
            nonlocal res
            if idx == len(s):
                res.append(path[:])
                return

            for i in range(idx, len(s)):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    path.append(s[idx:i+1])
                    traverse(i+1, path)
                    path.pop()

        traverse(0, [])
        return res
