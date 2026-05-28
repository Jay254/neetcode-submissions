class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_sorted = sorted(s1)

        for i in range(len1-1, len2):
            s = sorted(s2[i-len1+1:i+1])
            if s == s1_sorted:
                return True
        
        return False