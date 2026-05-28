class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        prev, curr = 1, 1

        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp += curr
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += prev
            
            prev, curr = curr, temp


        return curr
