class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force, go through each temperature and loop until a higher temperature is reached O(n^2)
        # Optimal Solution, use a stack that keeps the highest current temperature and loop until the end.
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result