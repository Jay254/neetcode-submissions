class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if the height list is empty, there's no water to trap
        if not height:
            return 0

        # Initialize pointers for the left and right ends of the array
        left, right = 0, len(height) - 1
        # Variables to keep track of the maximum heights from the left and right ends
        left_max, right_max = 0, 0
        # Variable to accumulate the total amount of trapped water
        water_trapped = 0

        # Process elements until the two pointers meet
        while left < right:
            # If the height at the left pointer is less than the height at the right pointer
            if height[left] < height[right]:
                # Check if the current left height is greater than or equal to left_max
                if height[left] >= left_max:
                    # Update left_max to the current left height, as no water can be trapped here
                    left_max = height[left]
                else:
                    # Calculate water trapped at the current left position
                    # The trapped water is the difference between left_max and the current height
                    water_trapped += left_max - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # If the height at the right pointer is less than or equal to the left pointer height
                # Check if the current right height is greater than or equal to right_max
                if height[right] >= right_max:
                    # Update right_max to the current right height, as no water can be trapped here
                    right_max = height[right]
                else:
                    # Calculate water trapped at the current right position
                    # The trapped water is the difference between right_max and the current height
                    water_trapped += right_max - height[right]
                # Move the right pointer to the left
                right -= 1

        # Return the total amount of trapped water after both pointers meet
        return water_trapped
