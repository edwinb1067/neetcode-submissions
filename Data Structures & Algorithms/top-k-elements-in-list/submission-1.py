from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = count.most_common(k)
        submit = []
        for i in range(k):
            submit.append(ans[i][0])
        return submit