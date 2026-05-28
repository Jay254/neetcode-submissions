class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #edge case for this
        # a tree of n nodes has exactly n-1 edges
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0,-1):
            return False


        return len(visited) == n