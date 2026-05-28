class Solution:
    def reorganizeString(self, s: str) -> str:
        cnts = Counter(s)
        heap = [(-cnt,ch) for ch, cnt in cnts.items()]
        heapq.heapify(heap)

        new = ""

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            new += ch1 + ch2

            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1+1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2+1, ch2))

        if heap:
            cnt, ch = heapq.heappop(heap)
            if -cnt > 1:
                return ""
            new += ch

        return new