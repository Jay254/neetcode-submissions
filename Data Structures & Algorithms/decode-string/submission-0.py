class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = 0

        for ch in s:
            if ch == '[':
                stack.append((res, num))
                res = ""
                num = 0
            elif ch == ']':
                prev, num = stack.pop()
                res = prev + res * num
                num = 0
            elif ch.isdigit():
                num = num * 10 + int(ch)
            else:
                res += ch

        return res