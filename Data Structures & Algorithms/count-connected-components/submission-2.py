class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)


        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                count += 1

        return count