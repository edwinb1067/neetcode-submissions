class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        stack = []
        pair = sorted(zip(position, speed), reverse=True)

        for pdx, spd in pair:
            time = (target - pdx) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        while stack:
            stack.pop()
            result += 1

        return result