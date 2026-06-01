class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        longest = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            max_freq = max(max_freq, dic[s[r]])
            
            while (r - l + 1) - max_freq > k:
                dic[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest