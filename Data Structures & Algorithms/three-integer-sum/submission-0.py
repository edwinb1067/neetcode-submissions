class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force, for each value have another value and search for the third value O(n^3)
        # Better Solution, Sort the list and do a two sum for each value
        order = sorted(nums)
        ans = []
        for i, num in enumerate(order):
            if i > 0 and order[i] == order [i-1]:
                continue
            left, right = i + 1, len(order) - 1
            while left < right:
                amount = order[left] + order[right]
                if amount == - num:
                    ans.append([num, order[left], order[right]])
                    while left < right and order[left] == order[left + 1]:
                        left += 1
                    while left < right and order[right] == order[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif amount > - num:
                    right -= 1
                else:
                    left += 1
            
        return ans