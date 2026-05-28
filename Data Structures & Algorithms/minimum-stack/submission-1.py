class MinStack:

    def __init__(self):
        self.stack = []  # This will hold all the values
        self.min_stack = []  # This will hold the minimum values

    def push(self, val: int) -> None:
        # Push the value to the main stack
        self.stack.append(val)
        
        # If the min stack is empty, or the new value is smaller than the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        val = self.stack.pop()
        
        # If the popped value is the minimum, pop it from the min stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The minimum value is always the top of the min stack
        return self.min_stack[-1]