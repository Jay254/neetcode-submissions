class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = '0000'
        if start in dead:
            return -1
        if start == target:
            return 0

        queue = deque([(start,0)])
        visited = {start}

        while queue:
            state, steps = queue.popleft()

            for i in range(4):
                for d in [-1,1]: # {-1,1} up or down
                    digit = (int(state[i]) + d) % 10 #wrap around
                    new_state = state[:i] + str(digit) + state[i+1:]

                    if new_state == target:
                        return steps + 1
                    if new_state not in dead and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps+1))

        return -1
