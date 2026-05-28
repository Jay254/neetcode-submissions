from collections import defaultdict,deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        #adjacency list created
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent: #skip parent
                    continue
                if not dfs(neighbor,node): #if any neighbor leads to a cycle
                    return False

            return True #all neighbors been visited

        if not dfs(0,-1): #check for cycles and connectivity
            return False 

        return len(visited) == n #Ensure all nodes are visited
        