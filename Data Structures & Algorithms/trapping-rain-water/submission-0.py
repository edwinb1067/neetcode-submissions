class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        sum_water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                if height[left] == max_left:
                    continue
                sum_water += min(max_left, max_right) - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                if height[right] == max_right:
                    continue
                sum_water += min(max_left, max_right) - height[right]

        return sum_water