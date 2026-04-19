class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to push parenthesis on until they get there back and then pop()
        stack = []
        for symbol in s:
            if symbol == "[" or symbol == "{" or symbol == "(":
                stack.append(symbol)
            elif not stack:
                return False
            elif symbol == "}":
                if stack.pop() != "{":
                    return False
            elif symbol == "]":
                if stack.pop() != "[":
                    return False
            else:
                if stack.pop() != "(":
                    return False
        return len(stack) == 0