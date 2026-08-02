class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for t in tokens:
            if t in '+-*/':
                n2 = self.stack.pop()
                n1 = self.stack.pop()
                if t == '+':
                    self.stack.append(n1 + n2)
                elif t == '-':
                    self.stack.append(n1 - n2)
                elif t == '*':
                    self.stack.append(n1 * n2)
                elif t == '/':
                    self.stack.append(int(n1/n2))
            else:
                self.stack.append(int(t))

        return self.stack[-1]