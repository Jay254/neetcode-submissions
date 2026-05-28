class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        def expandOutward(left, right):
            count = 0
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count+= 1
            return count

        palindromes = 0
        for i in range(len(s)):
            palindromes += expandOutward(i,i)
            palindromes += expandOutward(i,i+1)

        return palindromes

            