class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        new_p = sorted(zip(position, speed), reverse=True)

        for p, s in new_p:
            t = (target-p) / s

            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)