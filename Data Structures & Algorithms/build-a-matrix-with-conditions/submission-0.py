class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k+1)
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            order = []
            queue = deque([i for i in range(1,k+1) if indegree[i] == 0])

            while queue:
                vertice = queue.popleft()
                order.append(vertice)

                for nei in graph[vertice]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

            return order if len(order) == k else []


        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        rows = {num:i for i, num in enumerate(row_order)}
        cols = {num:i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1,k+1):
            r = rows[num]
            c = cols[num]
            matrix[r][c] = num

        return matrix
