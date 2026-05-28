class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        results = [None for i in range(n)]
        #print(len(position))
        for i in range(n):
            distance = target - position[i]
            time = distance/speed[i]
            results[i] = (position[i], time)

        results = sorted(results, reverse=True)

        #print(results)
        fleet_count = 0
        last_time = 0

        for i in results:
            pos, time = i
            #print(pos, time)
            if time > last_time:
                fleet_count += 1
                last_time = time

        return fleet_count
