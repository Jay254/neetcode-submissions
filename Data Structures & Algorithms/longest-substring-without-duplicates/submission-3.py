class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        right = 0
        a = set()
        max_size = 0

        while right < len(s):
            if s[right] not in a:
                a.add(s[right])
                right += 1
                max_size = max(max_size, right-left)
            else:
                a.remove(s[left])
                left += 1

        return max_size