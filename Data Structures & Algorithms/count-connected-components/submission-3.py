class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                count += 1

        return count