class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            dist = (point[0] ** 2 + point[1] ** 2)
            heap.append((dist, point))

        heapq.heapify(heap)
        closest = []
        while k > 0:
            _, point = heapq.heappop(heap)
            closest.append(point)
            k -= 1

        return closest