class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force approach would go through each element of the list and compare it to all other elements after it. O(n^2)
        # Better approach use a Hash Set and continue adding values only if the value is not already in the set, return false otherwise. O(n)
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False