class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0
        n = len(gas)

        for i in range(n):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1