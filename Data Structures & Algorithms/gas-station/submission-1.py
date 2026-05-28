class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum(gas) < sum(cost):
        #     return -1
        # start = 0
        # total_tank = 0
        # cur_tank = 0

        # for i in range(len(gas)):
        #     diff = gas[i] - cost[i]
        #     total_tank +=diff
        #     cur_tank += diff

        #     if cur_tank < 0:
        #         start = i + 1
        #         cur_tank = 0

        # return start if total_tank >= 0 else -1

        #NEETCODE
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1

        return start