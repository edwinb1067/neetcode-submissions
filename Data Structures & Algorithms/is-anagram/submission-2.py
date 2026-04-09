from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        for char in t:
            d[char] -= 1
        all_zero = all(value == 0 for value in d.values())
        return all_zero