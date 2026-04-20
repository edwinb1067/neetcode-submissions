class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"{":"}", "[":"]", "(":")"}
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
                continue
                
            if not stack:
                return False

            if char != pair[stack.pop()]:
                return False
        return len(stack) == 0
