class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target = Counter(s1)
        need = len(target)
        have = 0

        window = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            ch = s2[r]
            window[ch] += 1

            if ch in target and window[ch] == target[ch]:
                have += 1

            while r - l + 1 > len(s1):
                left = s2[l]

                if left in target and window[left] == target[left]:
                    have -= 1

                window[left] -= 1
                l += 1

            if have == need:
                return True


        return False