class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force, compare all boxes of water and return the highest O(n^2)
        # Better solution, Use two pointer and track the max height, iterating the lower bar
        left, right = 0, len(heights) - 1
        max_height = 0
        while left < right:
            water = min(heights[left], heights[right])*(right-left)
            if water > max_height:
                max_height = water
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_height