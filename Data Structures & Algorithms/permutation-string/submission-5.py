class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # brute force - sorting is expensive
        # len1, len2 = len(s1), len(s2)
        # if len1 > len2:
        #     return False

        # s1_sorted = sorted(s1)

        # for i in range(len1-1, len2):
        #     s = sorted(s2[i-len1+1:i+1])
        #     if s == s1_sorted:
        #         return True
        
        # return False
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        #only working on count2 right now
        for i in range(len1, len2):
            count2[ord(s2[i]) - ord('a')] += 1 #adding new character
            count2[ord(s2[i-len1]) - ord('a')] -= 1 #removing left most character
            if count1 == count2:
                return True

        return False