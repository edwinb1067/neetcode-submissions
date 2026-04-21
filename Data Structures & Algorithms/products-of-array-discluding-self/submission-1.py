class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get an array of everything before and after and the make a final array with both times each other
        pre = [1]
        post = [1]
        ans = []
        # Adds every value post and pre
        for i in range (1, len(nums) + 1):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[len(nums)-i])
        
        for j in range (0, len(nums)):
            ans.append(pre[j]*post[len(nums)-j-1])

        return ans