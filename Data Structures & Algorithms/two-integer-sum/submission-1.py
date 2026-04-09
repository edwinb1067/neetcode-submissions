class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, num in enumerate(nums):
            if my_map.get(target-num) is not None:
                return [my_map.get(target-num), i]
            my_map[num] = i
        return []