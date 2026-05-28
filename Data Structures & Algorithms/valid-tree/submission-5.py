class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        #dfs, detect cycles, tree 
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        stack = [(0, -1)]
        visited = set()

        while stack:
            node, parent = stack.pop()
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))

        return len(visited) == n