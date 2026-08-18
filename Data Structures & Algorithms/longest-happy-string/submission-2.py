class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        heapq.heapify(heap)

        while heap and heap[0][0] == 0:
            heapq.heappop(heap)

        s = ''
        while heap:
            count, ch = heapq.heappop(heap)
            if len(s) >= 2 and s[-1] == ch and s[-2] == ch:
                if not heap:
                    break

                c2, ch2 = heapq.heappop(heap)
                heapq.heappush(heap, (count, ch))

                s += ch2
                if c2 + 1 != 0:
                    heapq.heappush(heap, (c2+1, ch2))
            
            else:
                s += ch
                if count + 1 != 0:
                    heapq.heappush(heap, (count+1, ch))

        return s