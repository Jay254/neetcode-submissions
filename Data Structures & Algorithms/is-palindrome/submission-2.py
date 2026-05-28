class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s)).lower()
        #new_s.tolower()
        print(new_s)
        #"wasitacarisaworacatisaw"
        #left = 
        left = 0
        right = len(new_s)-1
        print(left, right)

        while left <= right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
