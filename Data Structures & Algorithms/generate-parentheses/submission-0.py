class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [( "", 0, 0 )]  # (current_string, open_count, close_count)

        while stack:
            current, open_count, close_count = stack.pop()

            # If the current string is of the maximum length, add it to results
            if len(current) == 2 * n:
                result.append(current)
                continue
            
            # Add an opening parenthesis if we still have one left to add
            if open_count < n:
                stack.append((current + '(', open_count + 1, close_count))
            
            # Add a closing parenthesis if it won't exceed the number of opening ones
            if close_count < open_count:
                stack.append((current + ')', open_count, close_count + 1))

        return result
