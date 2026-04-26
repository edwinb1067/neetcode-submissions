class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the key value will be it and the value would be the next value needed
        my_set = set(nums)
        max_count = 0

        for num in nums:
            if not num - 1 in my_set:
                length = 1
                while num + length in my_set:
                    length += 1
                max_count = int(max(max_count, length))

        return max_count