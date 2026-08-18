class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1]) #by pickup

        heap = [] #by (dropoff, passengers)
        cur = 0

        for cap, start, end in trips:
            while heap and heap[0][0] <= start:
                e, p = heapq.heappop(heap)
                cur -= p
            cur += cap
            if cur > capacity:
                return False
            heapq.heappush(heap, (end, cap))

        return True