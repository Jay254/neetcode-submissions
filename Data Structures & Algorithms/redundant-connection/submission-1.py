class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def bfs(start, target):
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for u,v in edges:
            if u in graph and v in graph and bfs(u,v):
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)

        return []