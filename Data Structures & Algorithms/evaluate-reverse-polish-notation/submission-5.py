class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        # Stack to store numbers during evaluation
        stack = []

        # Iterate over each token
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                val1 = int(stack.pop())  # Pop the first operand
                val2 = int(stack.pop())  # Pop the second operand

                if i == "+":
                    stack.append(val2 + val1)  # Perform addition
                elif i == "-":
                    stack.append(val2 - val1)  # Perform subtraction
                elif i == "*":
                    stack.append(val2 * val1)  # Perform multiplication
                else:  # Division
                    # Ensure division truncates toward zero
                    stack.append(int(val2 / val1) if val2 * val1 >= 0 else -(-val2 // val1))
            else:
                # If it's a number, convert it to an integer and push it onto the stack
                stack.append(int(i))

        # The final result is the only value left in the stack
        return stack.pop()