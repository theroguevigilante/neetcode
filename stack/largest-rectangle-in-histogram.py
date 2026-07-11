class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ci, ch = stack.pop()
                maxArea = max(maxArea, ch*(i - ci))
                start = ci
            stack.append((start, h))
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea
