import random

class Dice:
    def __init__(self, color: str, value: int) -> None:
        """
        Initialize a Dice object with a specified color and value.

        :param color: The color of the dice.
        :param value: The initial value of the dice.
        """
        if value == 0 or value > 6:
            self.value = random.randint(1, 6)
        else:
            self.value = value
        self.color = color

    def roll(self) -> None:

        self.value = random.randint(1, 6)


    def get_value(self) -> int:

        return self.value
    
    
    def get_color(self) -> str:

        return self.color
    
    
    def get_board(self, boards):

        for board in boards:
            if board.color == self.color:
                return board
            
            
    def print_color_value(self) -> str:

        colors = {
            "Yellow": "\033[93m",  # Yellow color code
            "Blue": "\033[94m",    # Blue color code
            "White": "\033[0m",    # Reset to default color
            "Green": "\033[92m",   # Green color code
            "Orange": "\033[91m",  # Orange color code
            "Purple": "\033[95m"   # Purple color code
        }

        color_code = colors.get(self.color, "")  # Get color code for the dice color

        if color_code:
            return f"{color_code}{self.value}\033[0m"  # Apply color to the dice value
        else:
            return str(self.value)  # If color not found, return the plain value
