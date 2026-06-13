class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        
        for x,y in points:
            heapq.heappush(heap, (x*x + y*y, [x,y]))

        for _ in range(k):
            _, arr = heapq.heappop(heap)
            res.append(arr)

        return res