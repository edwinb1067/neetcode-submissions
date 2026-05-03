class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Find a mechanism to push the furthest position to the bottom and then calculate how many car fleets there are
        result = 0
        stack = []
        pairs = sorted(zip(position, speed), reverse = True)
        # Loop through and get number fleets
        for pos, spd in pairs:
            curr_time = (target - pos) / spd
            stack.append(curr_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)