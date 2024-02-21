from clever.space import Space

class Board:
    def __init__(self, color: str, all_spaces: list[Space]) -> None:
        self.color = color
        self.all_spaces = all_spaces

    def get_color(self) -> str:
        return self.color

    def print_color_value(self) -> str:
        colors = {
            "Yellow": "\033[93m",  # Yellow color code
            "Blue": "\033[94m",    # Blue color code
            "White": "\033[0m",    # Reset to default color
            "Green": "\033[92m",    # Green color code
            "Orange": "\033[91m",   # Orange color code
            "Purple": "\033[95m"    # Purple color code
        }

        color_code = colors.get(self.color, "")  # Get color code for the dice color

        if color_code:
            return f"{color_code}{self.color}\033[0m"  # Apply color to the dice value
        else:
            return str(self.value)  # If color not found, return the plain value
    
    def get_all_spaces(self) -> list[Space]:
        return self.all_spaces

    def cross_space(self, space: Space, dice_value: int)  -> None:
        space.cross(dice_value)

        print(f"\nUpdated state of the {self.color} Board:")
        for space in self.all_spaces:
            if space.crossed:
                print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
            else:
                print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")

        print("\033[0m")

    def not_crossed_spaces(self) -> list[Space]:  
        not_crossed_list = []
        for space in self.all_spaces:
            if not space.crossed:
                not_crossed_list.append(space)
        return not_crossed_list

    def get_score(self) -> int:
        pass

    def is_crossable(self, space: Space, dice_value: int) -> None:
        pass

    def available_spaces(self, dice_value) -> list[Space]:
        available_spaces_list = []
        for s in self.all_spaces:
            if self.is_crossable(s, dice_value):
                available_spaces_list.append(s)

        return available_spaces_list