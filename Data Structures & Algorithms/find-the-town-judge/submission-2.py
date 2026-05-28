class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trusted = defaultdict(int)
        # people = {i for i in range(1,n+1)}
        # for a,b in trust:
        #     people.discard(a)
        #     trusted[b] += 1

        # if len(people) != 1:
        #     return -1

        # judge = list(people)[0]
        # return judge if trusted[judge]  == n-1 else -1

        in_degree = [0] * (n+1) #people that trust you
        out_degree = [0] * (n+1) #people you trust
        for u, v in trust:
            in_degree[v] += 1
            out_degree[u] += 1

        for i in range(1, n+1):
            if in_degree[i] == n-1 and out_degree[i] == 0:
                return i

        return -1