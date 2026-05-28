class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)

        # def bfs(start, target):
        #     queue = deque([start])
        #     visited = set([start])
        #     while queue:
        #         node = queue.popleft()

        #         if node == target:
        #             return True

        #         for neighbor in graph[node]:
        #             if neighbor not in visited:
        #                 visited.add(neighbor)
        #                 queue.append(neighbor)

        # for u,v in edges:
        #     if u in graph and v in graph and bfs(u,v):
        #         return [u,v]

        #     graph[u].append(v)
        #     graph[v].append(u)

        # return []
        parent, rank = {}, {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        for u,v in edges:
            if u not in parent:
                parent[u], rank[u] = u, 0
            if v not in parent:
                parent[v], rank[v] = v, 0
            if not union(u,v):
                return [u,v]