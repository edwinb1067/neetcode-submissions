class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tk in tokens:
            if tk in "*+-/":
                if tk == "*":
                    tk = stack.pop() * stack.pop()
                elif tk == "+":
                    tk = stack.pop() + stack.pop()
                elif tk == "-":
                    tk = - stack.pop() + stack.pop()
                else:
                    tk = (1 / stack.pop()) * stack.pop()
            stack.append(int(tk))
        return stack[-1]