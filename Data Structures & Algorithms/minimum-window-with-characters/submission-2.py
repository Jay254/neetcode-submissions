class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_count = len(need)
        left = have = 0
        window = defaultdict(int)
        res = [float('inf'), 0, 0]

        for right, ch, in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if right - left + 1 < res[0]:
                    res = [right-left+1, left, right]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res[1], res[2]

        return s[l:r+1] if res[0] != float('inf') else ""