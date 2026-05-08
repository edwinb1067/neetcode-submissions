class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Have two pointers that calculate total water, iterate the smaller height between them
        left, right = 0, len(heights) - 1
        biggest = 0
        while left < right:
            height = min(heights[left], heights[right]) * (right - left)
            biggest = max(biggest, height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return biggest