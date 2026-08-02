class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        stack = []
        for _, t in cars:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)