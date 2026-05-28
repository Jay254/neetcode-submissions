class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        rem_nodes = n

        while rem_nodes > 2:
            leaves_len = len(leaves)
            rem_nodes -= leaves_len

            for _ in range(leaves_len):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)