class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        #freq of char in t
        t_count = Counter(t)

        #vars for cur window and count of characters
        window_count = {}
        have, need = 0, len(t_count)

        #pointers for window
        left = 0
        min_length = float('inf')
        res = [-1,-1] #start and end of sliding window

        #expand window by moving right pointer
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char,0) + 1

            #check if needed
            if char in t_count and window_count[char] == t_count[char]:
                have += 1


            #when valid window happen
            while have == need:
                #update cur window
                if (right-left+1)<min_length:
                    min_length=right-left+1
                    res = [left,right]

                #remove character from left window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]]<t_count[s[left]]:
                    have -= 1

                left += 1 #shrink window
        left,right = res
        return s[left:right+1] if min_length != float('inf') else ''

