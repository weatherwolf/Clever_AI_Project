import random
import numpy as np
import warnings

from clever.player import Player
from clever.board import Board
from clever.round import Round
# from clever. ai import AI_Model

# class Space:
#     def __init__(self, crossed: bool, value: int, dice_value: int, index: int) -> None:
#         self.crossed = crossed
#         self.value = value
#         self.dice_value = dice_value
#         self.index = index

#     def cross(self, value: int = None):
#         self.crossed = True
#         if value is not None:
#             self.dice_value = value
        

# class Dice:
#     def __init__(self, color: str, value: int) -> None:
#         if value == 0 or value > 6:
#             self.value = random.randint(1, 6)
#         else:
#             self.value = value
#         self.color = color

#     def roll(self) -> None:
#         self.value = random.randint(1, 6)

#     def get_value(self) -> int:
#         return self.value
    
#     def get_color(self) -> str:
#         return self.color
    
#     def get_board(self, boards):
#         for board in boards:
#             if board.color == self.color:
#                 return board
            
#     def print_color_value(self) -> str:
#         colors = {
#             "Yellow": "\033[93m",  # Yellow color code
#             "Blue": "\033[94m",    # Blue color code
#             "White": "\033[0m",    # Reset to default color
#             "Green": "\033[92m",    # Green color code
#             "Orange": "\033[91m",   # Orange color code
#             "Purple": "\033[95m"    # Purple color code
#         }

#         color_code = colors.get(self.color, "")  # Get color code for the dice color

#         if color_code:
#             return f"{color_code}{self.value}\033[0m"  # Apply color to the dice value
#         else:
#             return str(self.value)  # If color not found, return the plain value

    
# class Board:
#     def __init__(self, color: str, all_spaces: list[Space]) -> None:
#         self.color = color
#         self.all_spaces = all_spaces

#     def get_color(self) -> str:
#         return self.color

#     def print_color_value(self) -> str:
#         colors = {
#             "Yellow": "\033[93m",  # Yellow color code
#             "Blue": "\033[94m",    # Blue color code
#             "White": "\033[0m",    # Reset to default color
#             "Green": "\033[92m",    # Green color code
#             "Orange": "\033[91m",   # Orange color code
#             "Purple": "\033[95m"    # Purple color code
#         }

#         color_code = colors.get(self.color, "")  # Get color code for the dice color

#         if color_code:
#             return f"{color_code}{self.color}\033[0m"  # Apply color to the dice value
#         else:
#             return str(self.value)  # If color not found, return the plain value
    
#     def get_all_spaces(self) -> list[Space]:
#         return self.all_spaces

#     def cross_space(self, space: Space, dice_value: int)  -> None:
#         space.cross(dice_value)

#         print(f"\nUpdated state of the {self.color} Board:")
#         for space in self.all_spaces:
#             if space.crossed:
#                 print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
#             else:
#                 print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")

#         print("\033[0m")

#     def not_crossed_spaces(self) -> list[Space]:  
#         not_crossed_list = []
#         for space in self.all_spaces:
#             if not space.crossed:
#                 not_crossed_list.append(space)
#         return not_crossed_list

#     def get_score(self) -> int:
#         pass

#     def is_crossable(self, space: Space, dice_value: int) -> None:
#         pass

#     def available_spaces(self, dice_value) -> list[Space]:
#         available_spaces_list = []
#         for s in self.all_spaces:
#             if self.is_crossable(s, dice_value):
#                 available_spaces_list.append(s)

#         return available_spaces_list
    
# class Round:
#     def __init__(self) -> None:
#         self.white_dice = Dice("White", 0)
#         self.yellow_dice = Dice("Yellow", 0)
#         self.blue_dice = Dice("Blue", 0)
#         self.green_dice = Dice("Green", 0)
#         self.orange_dice = Dice("Orange", 0)
#         self.purple_dice = Dice("Purple", 0)

#         self.all_dice = [self.white_dice, self.blue_dice, self.yellow_dice, self.green_dice, self.orange_dice, self.purple_dice]
#         self.usable_dice = [self.white_dice, self.blue_dice, self.yellow_dice, self.green_dice, self.orange_dice, self.purple_dice]
#         self.throw_away_dice = []
#         self.chosen_dices = []

#     def roll_dice(self) -> None:
#         for dice in self.usable_dice:
#             dice.roll()

#     def choose_dice(self, chosen_dice: Dice, player_actions: int) -> None:
#         if chosen_dice:
#             if player_actions > 1:
#                 dice_to_remove = []
#                 self.chosen_dices.append(chosen_dice)

#                 for dice in self.usable_dice:
#                     if chosen_dice.value > dice.value:
#                         dice_to_remove.append(dice)

#                 for dice in dice_to_remove:
#                     self.throw_away_dice.append(dice)
#                     self.usable_dice.remove(dice)
                
#                 self.usable_dice.remove(chosen_dice)

#             else:
#                 self.chosen_dices.append(chosen_dice)
#                 self.usable_dice.remove(chosen_dice)
#                 for d in self.usable_dice:
#                     self.throw_away_dice.append(d)
#                     self.usable_dice.remove(d)
    
#     def get_dice(self) -> list[Dice]:
#         return self.usable_dice

# class Player:
#     def __init__(self, name: str, score: int, boards: list[Board], index: int, AI_Model = None) -> None:
#         self.name = name
#         self.score = score
#         self.boards = boards
#         self.index = index
#         self.reroll_count = 0
#         self.plusOne_count = 0
#         self.fox_count = 0
#         self.AI_Model = AI_Model

#         self.bonusses = []

#     def get_reroll_count(self) -> int:
#         return self.reroll_count 
    
#     def get_plusOne_count(self) -> int:
#         return self.plusOne_count 
    
#     def get_fox_count(self) -> int:
#         return self.fox_count 
    
#     def set_reroll_count(self, newValue: int) -> None:
#         self.reroll_count = newValue 
    
#     def set_plusOne_count(self, newValue: int) -> None:
#         self.plusOne_count = newValue
    
#     def set_fox_count(self, newValue: int) -> None:
#         self.fox_count = newValue

#     def get_total_score(self) -> int: 
#         total_score = 0
#         lowest_score_board = 70
#         for board in self.boards:
#             total_score += board.get_score()
#             if board.get_score() < lowest_score_board:
#                 lowest_score_board = board.get_score()

#         total_score += lowest_score_board * self.fox_count
        
#         return total_score
    
#     def get_name(self):
#         return self.name
    
#     def player_choose_dice(self, dice: list[Dice]) -> Dice:
#         return random.choice(dice)
    
#     def player_choose_board(self, boards: list[Board]) -> Board:
#         return random.choice(boards)
        
#     def player_choose_space(self, available_spaces: list[Space]) -> Space:
#         return random.choice(available_spaces)
    
#     def player_choose_reroll(self) -> bool:
#         if self.reroll_count < 1:
#             warnings.warn("No reroll left, reroll_count of this player is non-positive", category=Warning)
#         return random.choice()
    
#     def player_choose_plusOne(self, dice: list[Dice]) -> Dice:
#         if self.plusOne_count < 1:
#             warnings.warn("No plusOne left, plusOne_count of this player is non-positive", category=Warning)
#         return random.choice(dice)


#     def choose_board(self, boards: list[Board], chosen_dice: Dice) -> Board:
#         if chosen_dice.get_color() == "White":
#             return self.player_choose_board(boards)
#         else:
#             return chosen_dice.get_board(boards)
    
#     def choose_space(self, board: Board, chosen_dice: Dice, round: Round) -> Space:
#         chosen_space = None
#         available_spaces = None
#         if board.color == "Blue":
#             available_spaces = board.available_spaces(round.white_dice.value + round.blue_dice.value)  
#         else:
#             available_spaces = board.available_spaces(chosen_dice.value)
        
#         if available_spaces:
#             chosen_space = self.player_choose_space(available_spaces)
#             chosen_space.cross(chosen_dice.get_value())

#         return chosen_space
    
    

#     def action(self, round: Round, dice: list[Dice]) -> Dice:
#         usable_dice = dice
#         bonus = []

#         print("Usable dice are")
#         for d in usable_dice:
#             print(d.print_color_value())

#         if usable_dice:
#             chosen_dice = self.player_choose_dice(usable_dice)
#             print(f"\n{self.name} choose {chosen_dice.print_color_value()}")

#             chosen_board = self.choose_board(self.boards, chosen_dice)

#             chosen_space = self.choose_space(chosen_board, chosen_dice, round)
#             print(f"\nThe available spaces on the {chosen_board.print_color_value()} board is: {chosen_space}")
#             if chosen_space:
#                 bonus = chosen_board.check_bonus(chosen_space)
#                 chosen_board.cross_space(chosen_space, chosen_dice.value)

#                 #bonusses is useless, need to change this soon
#                 if bonus:
#                     for b in bonus:
#                         self.bonusses.append(b)
#                         print(f"\nActing on the {b} bonus")
#                         chosen_space = b.power(player=self)


#             return chosen_dice
        
#         return None

#     def inactive_turn(self, round: Round) -> None:
#         print(f"\n Inactive turn of {self.name} \n")
#         self.action(round, round.throw_away_dice)
    
# class Bonus:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         pass
    
#     def get_name(self) -> str:
#         return self.name


# class Reroll(Bonus):
#     def __init__(self) -> None:
#         super().__init__("Reroll")

#     def power(player: Player) -> None:
#         player.set_plusOne_count(player.get_plusOne_count() + 1)

# class PlusOne(Bonus):
#     def __init__(self) -> None:
#         super().__init__("+1")

#     def power(player: Player) -> None:
#         player.set_plusOne_count(player.get_plusOne_count() + 1)


# class YellowX(Bonus):
#     def __init__(self) -> None:
#         super().__init__("Yellow X")

#     def power(player: Player) -> None:
#         spaces_to_choose = []
#         for board in player.boards:
#             if board.color == "Yellow":
#                 spaces_to_choose = board.not_crossed_spaces()
#         chosen_space: Space = player.player_choose_space(spaces_to_choose)
#         chosen_space.cross()


# class BlueX(Bonus):
#     def __init__(self) -> None:
#         super().__init__("Blue X")

#     def power(player: Player) -> None:
#         spaces_to_choose = []
#         for board in player.boards:
#             if board.color == "Blue":
#                 spaces_to_choose = board.not_crossed_spaces()
#         chosen_space = player.player_choose_space(spaces_to_choose)
#         print(f"Blue bonus activated, {player.get_name()} plays the space {chosen_space}")
#         chosen_space.cross()

# class GreenX(Bonus):
#     def __init__(self) -> None:
#         super().__init__(f"Green X")

#     def power(player: Player) -> None:
#         spaces_to_choose = []
#         for board in player.boards:
#             if board.color == "Green":
#                 spaces_to_choose = board.available_spaces(6)
#         chosen_space = player.player_choose_space(spaces_to_choose)
#         chosen_space.cross()

# class OrangeX(Bonus):
#     def __init__(self, number: int) -> None:
#         self.number = number
#         super().__init__(f"Orange {self.number}")

#     def power(self, player: Player) -> None:
#         spaces_to_choose = []
#         for board in player.boards:
#             if board.color == "Orange":
#                 spaces_to_choose = board.available_spaces(self.number)
#         chosen_space = player.player_choose_space(spaces_to_choose)
#         chosen_space.cross(self.number)

# class PurpleX(Bonus):
#     def __init__(self, number: int) -> None:
#         self.number = number
#         super().__init__("Purple {self.number}")

#     def power(self, player: Player) -> None:
#         spaces_to_choose = []
#         for board in player.boards:
#             if board.color == "Purple":
#                 spaces_to_choose = board.available_spaces(self.number)
#         chosen_space = player.player_choose_space(spaces_to_choose)
#         chosen_space.cross(self.number)

# class Fox(Bonus):
#     def __init__(self) -> None:
#         super().__init__("Fox")
    
#     def power(player: Player) -> None:
#         player.set_fox_count(player.get_fox_count() + 1)


# class YellowBoard(Board):
#     def __init__(self) -> None:
#         super().__init__('Yellow', [Space(False, 3, 0, 0), Space(False, 6, 0, 1), Space(False, 5, 0, 2), Space(True, 0, 0, 3),
#                                     Space(False, 2, 0, 4), Space(False, 1, 0, 5), Space(True, 0, 0, 6), Space(False, 5, 0, 7),
#                                     Space(False, 1, 0, 8), Space(True, 0, 0, 9), Space(False, 2, 0, 10), Space(False, 4, 0, 11),
#                                     Space(True, 0, 0, 12), Space(False, 3, 0, 13), Space(False, 4, 0, 14), Space(False, 6, 0, 15)])
        
#     def is_crossable(self, space: Space, dice_value: int) -> bool:
#         return (dice_value == 100  or space.value == dice_value) and not space.crossed

#     def check_bonus(self, space: Space)  -> list[Bonus]:
#         bonus_set = [BlueX, OrangeX(4), GreenX, Fox, PlusOne]
#         bonus = []
        
#         row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
#         if row_completed:
#             bonus.append(bonus_set[int(np.floor(space.index/4))])

#         if space.index in [0,5,10,15]:
#             diagnoal_completed = all(self.all_spaces[4*j + j].crossed for j in range(4))
#             if diagnoal_completed:
#                 bonus.append(bonus_set[4])
        
#         return bonus
  
#     def get_score(self) -> int:
#         score = 0
#         for i in range(4):
#             multiplier = 1
#             for j in range(4):
#                 if not self.all_spaces[4*j + i].crossed:
#                     multiplier = 0
#             if i <= 1:
#                 score += multiplier*(10 + 4*i)
#             elif i <= 3:
#                 score += multiplier*(8 + 4*i)
#         return score

# class BlueBoard(Board):
#     def __init__(self):
#         super().__init__('Blue', [Space(True, 0, 0, 0), Space(False, 2, 0, 1), Space(False, 3, 0, 2), Space(False, 4, 0, 3),
#                                    Space(False, 5, 0, 4), Space(False, 6, 0, 5), Space(False, 7, 0, 6), Space(False, 8, 0, 7),
#                                    Space(False, 9, 0, 8), Space(False, 10, 0, 9), Space(False, 11, 0, 10), Space(False, 12, 0, 11)])
        
#     def is_crossable(self, space: Space, dice_value: int) -> bool:
#         return (dice_value == 100 or space.value == dice_value) and not space.crossed

#     def get_score(self) -> int:
#         score = 0
#         count = 1
#         for space in self.all_spaces:
#             if space.crossed and not space.value == 0:
#                 if score == 0:
#                     score = 1
#                 else:
#                     score += count
#                     count += 1
#         return score
    
#     def check_bonus(self, space: Space) -> list[Bonus]:
#         bonus_set = [OrangeX(5), YellowX, Fox, Reroll, GreenX, PurpleX(6), PlusOne]
#         bonus = []
        
#         row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
#         if row_completed:
#             bonus.append(bonus_set[int(np.floor(space.index/4))])

#         column_completed = all(self.all_spaces[(space.index % 4) + 4*j].crossed for j in range(3))
#         if column_completed:
#             bonus.append(bonus_set[3 + (space.index % 4)])
        
#         return bonus

# class GreenBoard(Board):
#     def __init__(self) -> None:
#         super().__init__('Green', [Space(False, (i%5)+1, 0, i) for i in range(11)])
#         self.all_spaces[10].value = 6
    
#     def is_crossable(self, space: Space, dice_value: int) -> bool:
#         if not self.all_spaces[0].crossed:
#             return space.index == 0
        
#         else:
#             for i in range(1, 11):
#                 if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
#                     if dice_value > self.all_spaces[i].value: 
#                         return space.value == i
#         return False
            
#     def get_score(self) -> int:
#         score = 0
#         for space in self.all_spaces:
#             if not space.crossed:
#                 break
#             else:
#                 score += space.value
#         return score

#     def check_bonus(self, space: Space) -> list[Bonus]:
#         bonus_set = [PlusOne, BlueX, Fox, PurpleX(6), Reroll]
#         bonus = []
        
#         i = space.index
#         if i == 3:
#             bonus.append(bonus_set[0])
#         elif i == 5:
#             bonus.append(bonus_set[1])
#         elif i == 6:
#             bonus.append(bonus_set[2])
#         elif i == 8:
#             bonus.append(bonus_set[3])
#         elif i == 9:
#             bonus.append(bonus_set[4])
        
#         return bonus

# class OrangeBoard(Board):
#     def __init__(self) -> None:
#         super().__init__('Orange', [Space(False, i, 0, i) for i in range(11)])

#     def is_crossable(self, space: Space, dice_value: int) -> bool:
#         if not self.all_spaces[0].crossed:
#             return space.value == 0
        
#         else:
#             for i in range(1, 11):
#                     if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
#                         return space.value == i
        
#         return False

#     def cross_space(self, space: Space, dice_value: int) -> None:
#         if not space.crossed:
#             if space == self.all_spaces[3] or space == self.all_spaces[6] or space == self.all_spaces[8]:
#                 space.cross(2 * dice_value)
#             elif space == self.all_spaces[10]:
#                 space.cross(3 * dice_value)
#             else:
#                 space.cross(dice_value)
#         # else:
#         #     warnings.warn("Space has already been crossed, something went wrong", category=Warning)

#         print(f"\nUpdated state of the {self.color} Board:")
#         for space in self.all_spaces:
#             if space.crossed:
#                 print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
#             else:
#                 print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")


#     def get_score(self) -> int:
#         score = 0
#         for space in self.all_spaces:
#             if space.crossed:
#                 score += space.dice_value
#         return score
    
#     def check_bonus(self, space: Space) -> list[Bonus]:
#         bonus_set = [Reroll, YellowX, PlusOne, Fox, PurpleX(6)]
#         bonus = []
        
#         i = space.value
#         if i == 2:
#             bonus.append(bonus_set[0])
#         elif i == 4:
#             bonus.append(bonus_set[1])
#         elif i == 5:
#             bonus.append(bonus_set[2])
#         elif i == 7:
#             bonus.append(bonus_set[3])
#         elif i == 9:
#             bonus.append(bonus_set[4])

        
#         return bonus
        
# class PurpleBoard(Board):
#     def __init__(self) -> None:
#         super().__init__('Purple', [Space(False, i, 0, i) for i in range(11)])

#     def is_crossable(self, space: Space, dice_value: int) -> bool:
#         if not self.all_spaces[0].crossed:
#             return space.index == 0
        
#         else:
#             for i in range(1, 11):
#                     if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
#                         if dice_value > self.all_spaces[i-1].dice_value or self.all_spaces[i-1].dice_value == 6:
#                             return space.index == i
   
#         return False

#     def get_score(self) -> int:
#         score = 0
#         for space in self.all_spaces:
#             if space.crossed:
#                 score += space.dice_value
#         return score
    
#     def check_bonus(self, space: Space) -> list[Bonus]:
#         bonus_set = [Reroll, BlueX, PlusOne, YellowX, Fox, Reroll, GreenX, OrangeX(6), PlusOne]
#         bonus = []
        
#         if(space.index >= 2):
#             bonus.append(bonus_set[space.index-2])
        
#         return bonus

class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.current_player_index = 0
        self.round_number = 1
        self.rounds = []
        self.number_of_rounds = self.number_of_Rounds()

    def number_of_Rounds(self) -> int:
        if np.size(self.players) < 3: 
            return 6
        elif np.size(self.players) == 3:
            return 5
        elif np.size(self.players) == 4:
            return 4
        else:
            return 0

    def start_game(self) -> None:
        print("Starting a new game!")
        self.number_of_Rounds()
        self.initialize_rounds()
        self.play_rounds()
        self.end_game()

    def initialize_rounds(self) -> None:
        for _ in range(len(self.number_of_rounds*self.players)):
            round = Round()
            self.rounds.append(round)

    def play_rounds(self) -> None:
        for i in range(self.number_of_rounds):
            print(f"\nRound {self.round_number}")
            for player in self.players:
                self.play_round(self.rounds[player.index + np.size(self.players) * i], player)
            self.round_number += 1
        

    def play_round(self, round: Round, player: Player) -> None:
        print(f"\n{player.name}'s turn:")
        self.play_turn(player, round)

    def play_turn(self, player: Player, round: Round) -> None:
        print("Rolling dice...")
        player_actions = 3

        while player_actions > 0:
            print(f"\nActions remaining: {player_actions}")
            round.roll_dice()
            chosen_dice = player.action(round, round.usable_dice)  

            #If last turn of the round, discard all the dice that are not chosen
            round.choose_dice(chosen_dice, player_actions)
            
            player_actions -= 1
        
        for p in self.players:
            if p != player:
                p.inactive_turn(round)
        

    def end_game(self) -> None:
        print("")
        for player in self.players:
            for board in player.boards:
                print(f"The score of the {board.print_color_value()} board is: {board.get_score()}")
            print(f"The bonuses of {player.name} are: {player.bonusses}")
            print(f"The final score of {player.name} is {player.get_total_score()}\n")
        
        print("")
        print("End of the Game")

class ScoreBoard:
    def __init__(self, boards: list[Board]) -> None:
        self.boards = boards

    def get_total_score(self) -> None:
        total_score = 0
        for board in self.boards:
            print(f"The score for the {board.color} board is: {board.get_score()}")
            total_score += board.get_score()
        return total_score
        