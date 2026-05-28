class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) == 1:
            return False
        arr = []
        dic = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        if s[0] in dic:
            return False

        for i in s:
            if i in dic:
                if arr and arr[-1] == dic[i]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(i)

        return len(arr) == 0