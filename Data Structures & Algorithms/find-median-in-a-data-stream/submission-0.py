class MedianFinder:

    def __init__(self):
        self.med = []

    def addNum(self, num: int) -> None:
        self.med.append(num)
        #self.med.sort()

    def findMedian(self) -> float:
        n = len(self.med)
        left = 0
        right = n-1
        #[1,2,3,4]
        self.med.sort()
        mid = (left+right) // 2
        if (n%2 == 0):
            median = self.med[mid] + self.med[math.ceil((left+right)/2)]
            return median/2
        else:
            return self.med[mid]
        