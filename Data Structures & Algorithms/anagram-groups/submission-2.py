class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize HashMap
        my_map = {}
        # Loop through all string in the list
        for string in strs:
            ans = [0] * 26
        # Loop through all the character in each string and add them to an array
            for char in string:
                ans[ord(char) - ord('a')] += 1
        # Append to the list in the value of the key map
            key = tuple(ans)
            if my_map.get(key) is None:
                my_map[key] = [string]
            else:
                my_map[key].append(string)
        # Return the values() of the HashMap
        return list(my_map.values())