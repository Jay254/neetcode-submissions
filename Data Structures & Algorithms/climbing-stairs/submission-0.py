class Solution:
    def climbStairs(self, n: int) -> int:
        # If n is 0 or 1, there's only one way to reach the top
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize base values
        first = 1  # Ways to reach step 1
        second = 2  # Ways to reach step 2
        
        # Calculate the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            # The current step count is the sum of the previous two steps
            current = first + second
            first = second  # Move the pointer to the next step
            second = current  # Move the pointer to the next step
        
        return second  # The final answer is in the 'second' variable