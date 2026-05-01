class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force, go through each height until you reach a lower bar and track the highest value O(n^2)
        max_count = 0

        # Go through each number in heights
        for i in range(len(heights)):
            # Initilize fields
            count = 0
            index = i
            curr_height = heights[i]
            # Loop backward until you reach a lower height or reach the end
            while index > 0 and curr_height <= heights[index - 1]:
                count += 1
                index -= 1
            index = i
            # Loop forward until you reach a lower height or reach the end
            while index < len(heights) - 1 and curr_height <= heights[index + 1]:
                count += 1
                index += 1

            max_count = max(max_count, (count + 1) * curr_height)

        return max_count