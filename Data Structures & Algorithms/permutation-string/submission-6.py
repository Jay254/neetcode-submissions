class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s_count = defaultdict(int)
        window_count = defaultdict(int)

        for ch in s1:
            s_count[ch] += 1

        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] += 1

            if (r - l + 1) > len(s1):
                window_count[s2[l]] -= 1

                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]

                l += 1

            if window_count == s_count:
                return True

        return False