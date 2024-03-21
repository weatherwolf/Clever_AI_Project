from clever.space import Space
from clever.bonus import Bonus

# reroll bonus, rerolls the dice and updates reroll_count
class Reroll(Bonus):

    def __init__(self) -> None:
        super().__init__("Reroll")

    def power(player) -> None:
    
        player.set_reroll_count(player.get_reroll_count() + 1)


# plusOne bonus, add one out of all the dice at the end of the round
# The player chooses a dice and adds this to their board
class PlusOne(Bonus):

    def __init__(self) -> None:
        super().__init__("+1")

    def power(player) -> None:
        
        player.set_plusOne_count(player.get_plusOne_count() + 1)


# YellowX bonus, lets the player cross a random yellow space
class YellowX(Bonus):

    def __init__(self) -> None:
        super().__init__("Yellow X")

    def power(player) -> None:
        
        spaces_to_choose: list[Space] = []
        for board in player.boards:
            if board.color == "Yellow":
                spaces_to_choose = board.not_crossed_spaces()
        chosen_space: Space = player.player_choose_space(spaces_to_choose)
        chosen_space.cross()


# BlueX bonus, lets the player cross a random blue space
class BlueX(Bonus):

    def __init__(self) -> None:
        super().__init__("Blue X")

    def power(player) -> None:
        
        spaces_to_choose: list[Space] = []
        for board in player.boards:
            if board.color == "Blue":
                spaces_to_choose = board.not_crossed_spaces()
        chosen_space: Space = player.player_choose_space(spaces_to_choose)
        print(f"Blue bonus activated, {player.get_name()} plays the space {chosen_space}")
        chosen_space.cross()


# GreenX bonus, lets the player cross the next green space 
class GreenX(Bonus):

    def __init__(self) -> None:
        super().__init__(f"Green X")

    def power(player) -> None:
        
        spaces_to_choose: list[Space] = []
        for board in player.boards:
            if board.color == "Green":
                spaces_to_choose = board.available_spaces(6)
        chosen_space: Space = player.player_choose_space(spaces_to_choose)
        chosen_space.cross()


# OrangeX bonus, lets the player cross the next orange space with the value given
class OrangeX(Bonus):

    def __init__(self, number: int) -> None:
        self.number = number
        super().__init__(f"Orange {self.number}")

    def power(self, player) -> None:
        
        spaces_to_choose: list[Space] = []
        for board in player.boards:
            if board.color == "Orange":
                spaces_to_choose = board.available_spaces(self.number)
        chosen_space: Space = player.player_choose_space(spaces_to_choose)
        chosen_space.cross(self.number)


# PurpleX bonus, lets the player cross the next purple space with the value given
class PurpleX(Bonus):

    def __init__(self, number: int) -> None:
        self.number = number
        super().__init__("Purple {self.number}")

    def power(self, player) -> None:
        
        spaces_to_choose: list[Space] = []
        for board in player.boards:
            if board.color == "Purple":
                spaces_to_choose = board.available_spaces(self.number)
        chosen_space: Space = player.player_choose_space(spaces_to_choose)
        chosen_space.cross(self.number)
        

# Fox bonus, adds a fox to the fox_count of the Player
class Fox(Bonus):

    def __init__(self) -> None:
        super().__init__("Fox")
    
    def power(player) -> None:
        
        player.set_fox_count(player.get_fox_count() + 1)

