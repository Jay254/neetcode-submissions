class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        left = right = 0
        seen = set()

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_len = max(max_len, right-left)
            else:
                seen.remove(s[left])
                left += 1

        return max_len