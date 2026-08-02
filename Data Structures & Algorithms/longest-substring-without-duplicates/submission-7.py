class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        longest = 0

        for j, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[i])
                i += 1

            longest = max(longest, j - i + 1)
            seen.add(ch)

        return longest
            