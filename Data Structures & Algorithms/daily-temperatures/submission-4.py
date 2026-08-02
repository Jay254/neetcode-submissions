class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while temps and temperatures[temps[-1]] < t:
                prev = temps.pop()
                res[prev] = i - prev
            temps.append(i)

        return res