class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with zeros, one for each day
        result = [0 for _ in range(len(temperatures))]
        
        # Stack to store indices of days with unresolved warmer temperature
        stack = []

        # Iterate through each day in the temperatures list
        for cur_day in range(len(temperatures)):
            # Check if the current day's temperature is higher than the temperature
            # of the day stored at the top of the stack
            while stack and temperatures[cur_day] > temperatures[stack[-1]]:
                prev_day = stack.pop()  # Get the index of the previous day
                # Calculate the number of days waited and store in the result
                result[prev_day] = cur_day - prev_day
            
            # Push the current day's index onto the stack
            # We haven't found a warmer temperature for this day yet
            stack.append(cur_day)

        # Return the result list containing days waited for each temperature
        return result
