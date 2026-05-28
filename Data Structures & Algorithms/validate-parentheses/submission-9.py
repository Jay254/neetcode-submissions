class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for ch in s:
            if ch in valid:
                if stack and stack[-1] == valid[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0