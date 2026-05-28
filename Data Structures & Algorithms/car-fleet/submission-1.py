class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        results = [None for i in range(n)]
        
        # Calculate time to reach the target for each car
        for i in range(n):
            distance = target - position[i]
            time = distance / speed[i]
            results[i] = (position[i], time)

        # Sort cars by starting position in descending order
        results = sorted(results, reverse=True)

        # Track fleets
        fleet_count = 0
        last_time = 0  # Initialize last time as zero
        
        for _, time in results:
            # Check if current car's time forms a new fleet
            if time > last_time:
                fleet_count += 1  # New fleet
                last_time = time  # Update last_time to current car's time
        
        return fleet_count
