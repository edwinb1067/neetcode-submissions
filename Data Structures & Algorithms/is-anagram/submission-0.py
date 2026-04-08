class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force, track each letter and compare two strings to see if they are equal
        # Better approach have one array that has all 26 characters and increment/decrement for both strings and make sure all values are zero at the end
        if s == None or t == None or len(s) != len(t):
            return s == t == ""
        alphabet = [0] * 26
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] -= 1
        for letter in alphabet:
            if letter != 0:
                return False
        return True