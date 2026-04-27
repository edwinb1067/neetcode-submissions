class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Get a stack of numbers and then once you hit the operator sign pop 2 values and then add them back to the stack
        stack = []

        for token in tokens:
            new = 0
            if token not in "+-*/":
                stack.append(int(token))
                continue
            elif token == "+":
                new = int(stack.pop()) + int(stack.pop())
            elif token == "*":
                new = int(stack.pop()) * int(stack.pop())
            elif token == "-":
                new = - int(stack.pop()) + int(stack.pop())
            else:
                new = (1 / int(stack.pop())) * int(stack.pop())
            stack.append(new)
        print(stack)
        return int(stack[-1])