class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force, go loop through each element and attempt to calculate the targe with every other element. O(n^2) O(1)
        # Better approach, loop through once adding what numbers are needed to calculate the target to a hashmap and then returning the index. O(n) O(n)
        my_map = {}
        for i in range(len(nums)):
            if nums[i] in my_map:
                return [my_map[nums[i]], i]
            my_map[target - nums[i]] = i
        return -1