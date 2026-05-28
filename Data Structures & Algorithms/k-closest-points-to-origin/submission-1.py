class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = ((x**2) + (y**2)) ** 0.5
            heapq.heappush(heap, (dist, [x,y]))

        res = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append([point[0], point[1]])

        return res