class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]  # Initialize with -1 to handle widths correctly

        for i in range(len(heights)):
            # Check if the current height is less than the height at the index in stack's top
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                # Pop the top of the stack
                popped = stack.pop()
                # Calculate the width of the rectangle with heights[popped] as the smallest height
                width = i - stack[-1] - 1  # Width between current index and new top of stack
                # Calculate area and update max_area
                area = heights[popped] * width
                max_area = max(max_area, area)
            # Push the current index onto the stack
            stack.append(i)

        # Clear the stack after the loop to calculate remaining areas
        while stack[-1] != -1:
            popped = stack.pop()
            width = len(heights) - stack[-1] - 1  # Calculate width to end of the array
            area = heights[popped] * width
            max_area = max(max_area, area)

        return max_area