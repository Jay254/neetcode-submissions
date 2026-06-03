class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    val = num1+num2
                elif token == '-':
                    val = num1-num2
                elif token == '*':
                    val = num1 * num2
                else:
                    val = int(num1 / num2)
                stack.append(val)
            else:
                stack.append(int(token))

        return stack[-1]
