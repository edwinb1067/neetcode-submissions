class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_count = 0

        for num in nums:
            if num - 1 in my_set:
                continue
            length = 0
            while num + length in my_set:
                length += 1
            max_count = max(max_count, length)
        
        return max_count