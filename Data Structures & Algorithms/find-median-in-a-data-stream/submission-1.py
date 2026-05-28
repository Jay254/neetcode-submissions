class MedianFinder:

    def __init__(self):
        self.small = [] #max heap
        self.large = [] #min heap

    def addNum(self, num: int) -> None:
        if self.small and num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        elif len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0]+self.large[0]) / 2
        return -self.small[0] if len(self.small) > len(self.large) else self.large[0]
        