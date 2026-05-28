class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0,0)] # dist, start pos
        n = len(points)
        visited = set()
        total_cost = 0


        while len(visited) < n:
            dist, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += dist

            for j in range(n):
                if j not in visited:
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    dist = abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap, (dist,j))

        return total_cost