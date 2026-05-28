class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr1 = []
        arr2 = []
        for i in range(len(s)):
            arr1.append(s[i])
            arr2.append(t[i])
        
        arr1.sort()
        arr2.sort()
        # print(arr1)
        # print(arr2)
        if arr1 == arr2:
            return True
        return False
