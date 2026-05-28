class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False

        new = ''.join(sorted(s1))
        s1_len = len(s1)
        s2_len = len(s2)
        window = []

        
        if s2_len < s1_len:
            return False

        # grab next s1_len elements and push them on our window
        for i in range(s2_len):
            cur = s2[i:i+s1_len]
            new_cur = ''.join(sorted(cur))
            print(new_cur, new)
            if new_cur == new:
                return True

        return False

        #print(new)