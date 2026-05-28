class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def extend(i,j):
            nonlocal count
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return s[i+1:j]


        longest = ""
        for i in range(n):
            odd = extend(i, i)
            even = extend(i, i+1)

        return count