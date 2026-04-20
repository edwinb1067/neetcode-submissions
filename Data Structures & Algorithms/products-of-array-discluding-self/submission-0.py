class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force, go through each element in nums and multiply all other elements by num O(n^2)
        # Better Solution, create an equal sized array with the product of every number and divide each number by its index in nums
        # Doesn't work when there is a zero
        # Optimal Solution, get the back n-1 product, store it (Do something special when 0)
        product = 1
        holder = 0
        ans = [0] * len(nums)
        is_zero = False
        for i in range (len(nums) - 1, 0, -1):

            if nums[i] == 0:
                holder = i
                ans[holder] = product
                is_zero = True
                break

            product *= nums[i]

        if is_zero:
            for j in range(holder - 1, -1, -1):
                ans[holder] *= nums[j]
            return ans

        for k in range (len(nums)):
            if k == 0:
                ans[k] = product
                continue

            ans[k] = int(ans[k-1] * nums[k-1] / nums[k])

        return ans


                