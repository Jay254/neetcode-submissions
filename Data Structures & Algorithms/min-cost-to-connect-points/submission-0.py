class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0,0)]
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)
            if curr in visited:
                continue

            total_cost += cost
            visited.add(curr)

            for nexti in range(n):
                if nexti not in visited:
                    x1, y1 = points[curr]
                    x2, y2 = points[nexti]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(min_heap, (dist, nexti))

        return total_cost