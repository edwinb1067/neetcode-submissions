class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force, for each temperature in temperatures find the next warmer day O(n^2)
        # Better Option, using a stack track the last warmest day and continut to pop off the back of the stack.
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result
