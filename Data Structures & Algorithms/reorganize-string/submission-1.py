class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for k,v in count.items():
            heapq.heappush(heap, (-v,k))

        s = ''
        while heap:
            count, ch = heapq.heappop(heap)
            if s and s[-1] == ch:
                if not heap:
                    return ''
                    
                c2, ch2 = heapq.heappop(heap)
                heapq.heappush(heap, (count, ch))
                s += ch2
                if c2+1 != 0:
                    heapq.heappush(heap, (c2+1, ch2))
            else:
                s += ch
                if count + 1 != 0: 
                    heapq.heappush(heap, (count+1, ch))

        return s