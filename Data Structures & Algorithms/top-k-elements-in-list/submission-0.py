from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force, go though the entire array for each character and add the number into the array O(n^2)
        # Sort and track the highest k elements after going through the loop O(nlog(n))
        # Better Solution, Use a dict to store each variable and the count of that variable O(n)
        count = Counter(nums)
        ans = list(count.most_common(k))
        ans2 = []
        for i in range(k):
            ans2.append(ans[i][0])
        return ans2            