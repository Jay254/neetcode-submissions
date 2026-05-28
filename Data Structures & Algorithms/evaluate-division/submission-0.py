class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b),val in zip(equations,values):
            graph[a][b] = val
            graph[b][a] = 1/val

        def dfs(cur, target, visited, acc):
            if cur == target:
                return acc
            visited.add(cur)
            for neighbor,w in graph[cur].items():
                if neighbor not in visited:
                    result = dfs(neighbor,target,visited,acc*w)
                    if result != -1.0:
                        return result

            return -1.0

        res = []
        for x,y in queries:
            if x not in graph or y not in graph:
                res.append(-1.0)
            elif x == y:
                res.append(1.0)
            else:
                res.append(dfs(x,y,set(),1.0))

        return res
            