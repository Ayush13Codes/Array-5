class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # T: O(n), S: O(1)
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  # Robot's position
        d = 0  # Initial direction is North

        for instr in instructions:
            if instr == "G":  # Move forward
                x += directions[d][0]
                y += directions[d][1]
            elif instr == "L":  # Turn left
                d = (d - 1) % 4
            elif instr == "R":  # Turn right
                d = (d + 1) % 4

        # The robot is bounded if it returns to origin or is not facing north
        return (x == 0 and y == 0) or d != 0
