class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        farthest = 0

        for i in range(n):
            if reachable[i]:
                start = max(farthest+1, i + minJump)
                end = min(i+maxJump, n-1)

                for j in range(start, end+1):
                    if s[j] == '0':
                        reachable[j] = True
                farthest = end

        return reachable[-1]
