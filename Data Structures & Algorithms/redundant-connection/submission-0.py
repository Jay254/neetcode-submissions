class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u,v in edges:
            if not u in parent:
                parent[u] = u
            if not v in parent:
                parent[v] = v
            if not union(u,v):
                return [u,v]