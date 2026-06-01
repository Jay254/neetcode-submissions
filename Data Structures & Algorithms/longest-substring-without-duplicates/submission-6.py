class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        j = 0
        max_len = 0
        for i in range(len(s)):
            while j < i and s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            max_len = max(max_len, i - j + 1)

        return max_len
