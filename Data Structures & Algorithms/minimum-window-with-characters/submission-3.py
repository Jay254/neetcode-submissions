class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = defaultdict(int)
        window_count = defaultdict(int)

        for ch in t:
            t_count[ch] += 1

        have, need = 0, len(t_count)
        res = [-1,-1] #left and right window
        result_len = float('inf')

        l = 0
        for r in range(len(s)):
            window_count[s[r]] += 1

            if s[r] in t_count and t_count[s[r]] == window_count[s[r]]:
                have += 1

            while have == need:
                window_len = r - l + 1

                if window_len < result_len:
                    result_len = window_len
                    res = [l, r]

                window_count[s[l]] -= 1

                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        l, r = res 
        if l == -1:
            return ""

        return s[l:r+1]
