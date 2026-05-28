class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def extend(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]


        longest = ""
        for i in range(n):
            odd = extend(i, i)
            even = extend(i, i+1)

            pali = odd if len(odd) > len(even) else even

            longest = pali if len(pali) > len(longest) else longest

        return longest
