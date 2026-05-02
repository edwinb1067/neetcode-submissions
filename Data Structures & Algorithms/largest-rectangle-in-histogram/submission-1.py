class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                result = max(result, height * (i - idx))
                start = idx
            stack.append((start, h))

        for start, height in stack:
            result = max(result, height * (len(heights) - start))
            
        return result