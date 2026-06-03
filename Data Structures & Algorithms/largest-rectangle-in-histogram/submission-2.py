class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                width = i - idx
                max_area = max(max_area, height * width) 
                start = idx

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area