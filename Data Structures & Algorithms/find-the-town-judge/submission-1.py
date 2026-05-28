class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_deg = [0] * (n+1) #people you trust
        in_deg = [0] * (n+1) #people that trust you

        for u,v in trust:
            out_deg[u] += 1
            in_deg[v] += 1

        for i in range(1, n+1):
            if out_deg[i] == 0 and in_deg[i] == n-1:
                return i

        return -1