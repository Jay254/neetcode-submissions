class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Handle edge cases
        if not nums or k == 0:
            return []
        if len(nums) < k:
            return [max(nums)]
        
        # Initialize the result list
        max_array = []
        
        # Iterate through the array to get each window's max
        for i in range(len(nums) - k + 1):
            # Define the window slice
            window = nums[i:i + k]
            # Find the max in the current window
            max_element = max(window)
            # Append max to the result list
            max_array.append(max_element)
        
        return max_array