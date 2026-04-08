class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force, go through each element, check if that element is in the list. O(n^2) time complexity O(1) Space Complexity
        # Optimal solution, use a hashset and if the value is already in the has set, return true.
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False