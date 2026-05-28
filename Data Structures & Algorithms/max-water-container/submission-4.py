class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        #l = 0
        # maxW = 0

        # for i, num in enumerate(heights):
        #     #i = i+1
        #     r = n-1
        #     while i < r:
        #         leng = r - i
        #         heigh = min(num, heights[r])
        #         print(leng, heigh)
        #         area = (leng * heigh)
        #         maxW = max(maxW, area)
        #         r -= 1

        # return maxW
        l = 0
        r = n-1
        maxArea = 0
        
        while l <= r:
            area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea

