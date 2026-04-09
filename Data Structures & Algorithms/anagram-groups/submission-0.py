from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force would be to go through each string and store the ones with the same letter output in different arrays and then return the final array of all the arrays
        # Make a hashmap of Lists that check whether the current hashmap array is already set
        my_map = {} # <HashMap<Char, Integer>, List<String>
        my_list = [] # List<String>
        # Go through each String and add their values to the HashMap
        for stri in strs:
            my_str = [0] * 26 # HashMap<Char, Integer>
            for char in stri:
                my_str[ord(char) - ord('a')] += 1
            key = tuple(my_str)
            if my_map.get(key):
                my_map.get(key).append(stri)
            else:
                new_list = [stri]
                my_map[key] = new_list
        return list(my_map.values())
