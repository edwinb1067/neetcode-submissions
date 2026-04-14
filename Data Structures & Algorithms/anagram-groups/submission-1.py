class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize HashMap and List
        my_map = {}
        for string in strs:
            ans = [0] * 26
            for char in string:
                ans[ord(char)-ord('a')] += 1
            key = tuple(ans)
            if my_map.get(key) is None:
                my_map[key] = [string]
            else:
                my_map[key].append(string)
        return list(my_map.values())

