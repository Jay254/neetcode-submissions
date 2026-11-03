class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for ch in s:
            if stack and ch in dic:
                if stack[-1] != dic[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0