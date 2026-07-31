class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for ch in s:
            if stack and ch in dic:
                if stack[-1] != dic[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack