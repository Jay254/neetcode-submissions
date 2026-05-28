class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        #l = 0
        maxW = 0

        for i, num in enumerate(heights):
            #i = i+1
            r = n-1
            while i < r:
                leng = r - i
                heigh = min(num, heights[r])
                print(leng, heigh)
                area = (leng * heigh)
                maxW = max(maxW, area)
                r -= 1

        return maxW
