class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        order = sorted(nums)
        for i, num in enumerate(order):
            if i > 0 and num == order[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                target = order[left] + order[right]
                if target == - num:
                    ans.append([num, order[left], order[right]])
                    while left < right and order[left] == order[left+1]:
                        left += 1
                    while left < right and order[right] == order[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif target > - num:
                    right -= 1
                else:
                    left += 1
        return ans
