import random
import numpy as np
import warnings

class Dice:
    def __init__(self, color, value):
        if value == 0 or value > 6:
            self.value = random.randint(1, 6)
        else:
            self.value = value
        self.color = color

    def roll(self):
        self.value = random.randint(1, 6)
    
    def get_board(self, boards):
        for board in boards:
            if board.color == self.color:
                return board
            
    def print_color_value(self):
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
            return f"{color_code}{self.value}\033[0m"  # Apply color to the dice value
        else:
            return str(self.value)  # If color not found, return the plain value
        

class ScoreBoard:
    def __init__(self, boards):
        self.boards = boards

    def get_total_score(self):
        total_score = 0
        for board in self.boards:
            print(f"The score for the {board.color} board is: {board.get_score()}")
            total_score += board.get_score()
        return total_score
        

class Space:
    def __init__(self, crossed, value, dice_value, index):
        self.crossed = crossed
        self.value = value
        self.dice_value = dice_value
        self.index = index

class Bonus:
    def __init__(self, type):
        self.type = type

    
class ColorBoard:
    def __init__(self, color, all_spaces):
        self.color = color
        self.all_spaces = all_spaces

    def get_color(self):
        return self.color
    
    def get_all_spaces(self):
        return self.all_spaces

    def cross_space(self, space, dice_value):
        space.crossed = True
        space.dice_value = dice_value

        # Display the updated state of the Chosen Board
        print(f"\nUpdated state of the {self.color} Board:")
        for space in self.all_spaces:
            if space.crossed:
                print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
            else:
                print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")

        print("\033[0m")


    def check_bonus(self, space):
        pass

    def get_score(self):
        pass

    def is_crossable(self, space, dice_value):
        pass

    def available_spaces(self, board, dice_value):
        available_spaces_list = []
        for s in board.all_spaces:
            if self.is_crossable(s, dice_value):
                available_spaces_list.append(s)

        return available_spaces_list

class YellowBoard(ColorBoard):
    def __init__(self):
        super().__init__('Yellow', [Space(False, 3, 0, 0), Space(False, 6, 0, 1), Space(False, 5, 0, 2), Space(True, 0, 0, 3),
                                    Space(False, 2, 0, 4), Space(False, 1, 0, 5), Space(True, 0, 0, 6), Space(False, 5, 0, 7),
                                    Space(False, 1, 0, 8), Space(True, 0, 0, 9), Space(False, 2, 0, 10), Space(False, 4, 0, 11),
                                    Space(True, 0, 0, 12), Space(False, 3, 0, 13), Space(False, 4, 0, 14), Space(False, 6, 0, 15)])
        
    def is_crossable(self, space, dice_value):
        return (dice_value == 100  or space.value == dice_value) and not space.crossed

    def check_bonus(self, space):
        bonus_set = ["Blue X", "Orange 4", "Green X", "Fox", "+1"]
        bonus = []
        
        row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
        if row_completed:
            bonus.append(bonus_set[int(np.floor(space.index/4))])

        if space.index in [0,5,10,15]:
            diagnoal_completed = all(self.all_spaces[4*j + j].crossed for j in range(4))
            if diagnoal_completed:
                bonus.append(bonus_set[4])
        
        return bonus
  
    def get_score(self):
        score = 0
        for i in range(4):
            multiplier = 1
            for j in range(4):
                if not self.all_spaces[4*j + i].crossed:
                    multiplier = 0
            if i <= 1:
                score += multiplier*(10 + 4*i)
            elif i <= 3:
                score += multiplier*(8 + 4*i)
        return score

class BlueBoard(ColorBoard):
    def __init__(self):
        super().__init__('Blue', [Space(True, 0, 0, 0), Space(False, 2, 0, 1), Space(False, 3, 0, 2), Space(False, 4, 0, 3),
                                   Space(False, 5, 0, 4), Space(False, 6, 0, 5), Space(False, 7, 0, 6), Space(False, 8, 0, 7),
                                   Space(False, 9, 0, 8), Space(False, 10, 0, 9), Space(False, 11, 0, 10), Space(False, 12, 0, 11)])
        
    def is_crossable(self, space, dice_value):
        return (dice_value == 100  or space.value == dice_value) and not space.crossed
    
    # def cross_space(self, dice_value):



    def get_score(self):
        score = 0
        count = 1
        for space in self.all_spaces:
            if space.crossed and not space.value == 0:
                if score == 0:
                    score = 1
                else:
                    score += count
                    count += 1
        return score
    
    def check_bonus(self, space):
        bonus_set = ["Orange 5", "Yellow X", "Fox", "Reroll", "Green X", "Purple 6", "+1"]
        bonus = []
        
        row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
        if row_completed:
            bonus.append(bonus_set[int(np.floor(space.index/4))])

        column_completed = all(self.all_spaces[(space.index % 4) + 4*j].crossed for j in range(3))
        if column_completed:
            bonus = bonus_set[4 + (space.index % 4)]
        
        return bonus

class GreenBoard(ColorBoard):
    def __init__(self):
        super().__init__('Green', [Space(False, (i%5)+1, 0, i) for i in range(11)])
        self.all_spaces[10].value = 6
    
    def is_crossable(self, space, dice_value):
        if self.all_spaces[0].crossed == False:
            return space.value == 0
        
        else:
            for i in range(1, 11):
                    if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                        if dice_value > self.all_spaces[i].value: 
                            return space.value == i
        
        return False
            
    def get_score(self):
        score = 0
        for space in self.all_spaces:
            if not space.crossed:
                break
            else:
                score += space.value
        return score

    def check_bonus(self, space):
        bonus_set = ["+1", "Blue X", "Fox", "Purple 6", "Reroll"]
        bonus = []
        
        i = space.index
        if i == 3:
            bonus.append(bonus_set[0])
        elif i == 5:
            bonus.append(bonus_set[1])
        elif i == 6:
            bonus.append(bonus_set[2])
        elif i == 8:
            bonus.append(bonus_set[3])
        elif i == 9:
            bonus.append(bonus_set[4])
        
        return bonus

class OrangeBoard(ColorBoard):
    def __init__(self):
        super().__init__('Orange', [Space(False, i, 0, i) for i in range(11)])

    def is_crossable(self, space, dice_value):
        if not self.all_spaces[0].crossed:
            return space.value == 0
        
        else:
            for i in range(1, 11):
                    if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                        return space.value == i
        
        return False

    def cross_space(self, space, dice_value):
        if not space.crossed:
            space.crossed = True
            if space == self.all_spaces[3] or space == self.all_spaces[6] or space == self.all_spaces[8]:
                space.dice_value = 2 * dice_value
            elif space == self.all_spaces[10]:
                space.dice_value = 3 * dice_value
            else:
                space.dice_value = dice_value
            print(f"\033[91mThe dice value is: {space.dice_value} \033[0m")
        else:
            warnings.warn("Space has already been crossed, something went wrong", category=Warning)

        print(f"\nUpdated state of the {self.color} Board:")
        for space in self.all_spaces:
            if space.crossed:
                print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
            else:
                print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")


    def get_score(self):
        score = 0
        for space in self.all_spaces:
            if space.crossed:
                score += space.dice_value
        return score
    
    def check_bonus(self, space):
        bonus_set = ["Reroll", "Yellow X", "+1", "Fox", "Purple 6"]
        bonus = []
        
        i = space.value
        if i == 2:
            bonus.append(bonus_set[0])
        elif i == 4:
            bonus.append(bonus_set[1])
        elif i == 5:
            bonus.append(bonus_set[2])
        elif i == 7:
            bonus.append(bonus_set[3])
        elif i == 9:
            bonus.append(bonus_set[4])

        
        return bonus
        
class PurpleBoard(ColorBoard):
    def __init__(self):
        super().__init__('Purple', [Space(False, i, 0, i) for i in range(11)])

    def is_crossable(self, space, dice_value):
        if not self.all_spaces[0].crossed:
            return space.value == 0
        
        else:
            for i in range(1, 11):
                    if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                        if dice_value > self.all_spaces[i-1].dice_value or self.all_spaces[i-1].dice_value == 6:
                            return space.value == i
                            
        
        return False


    def get_score(self):
        score = 0
        for space in self.all_spaces:
            if space.crossed:
                score += space.dice_value
        return score
    
    def check_bonus(self, space):
        bonus_set = ["Reroll", "Blue X", "+1", "Yellow X", "Fox", "Reroll", "Green X", "Orange 6", "+1"]
        bonus = []
        
        if(space.index >= 2):
            bonus.append(bonus_set[space.index-2])
        
        return bonus
    
class Bonus:
    def __init__(self, rerolls, extra_dice):
        self.rerolls = rerolls
        self.extra_dice = extra_dice

    def yellow_bonus(self):
        pass

class Round:
    def __init__(self):

        self.white_dice = Dice("White", 0)
        self.yellow_dice = Dice("Yellow", 0)
        self.blue_dice = Dice("Blue", 0)
        self.green_dice = Dice("Green", 0)
        self.orange_dice = Dice("Orange", 0)
        self.purple_dice = Dice("Purple", 0)

        self.all_dice = [self.white_dice, self.blue_dice, self.yellow_dice, self.green_dice, self.orange_dice, self.purple_dice]
        self.throw_away_dice = []
        self.chosen_dices = []

    def roll_dice(self):
        for dice in self.all_dice:
            dice.roll()

    def choose_dice(self, chosen_dice):
        dice_to_remove = []
        self.chosen_dices.append(chosen_dice)

        for dice in self.all_dice:
            if chosen_dice.value > dice.value:
                dice_to_remove.append(dice)

        for dice in dice_to_remove:
            self.throw_away_dice.append(dice)
            self.all_dice.remove(dice)
        
        self.all_dice.remove(chosen_dice)


class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.round_number = 1
        self.rounds = []

    def start_game(self):
        print("Starting a new game!")
        self.initialize_rounds()
        self.play_rounds()
        self.end_game()

    def initialize_rounds(self):
        for _ in range(5*len(self.players)):
            round = Round()
            self.rounds.append(round)

    def play_rounds(self):
        for i in range(5):
            print(f"\nRound {self.round_number}")
            for player in self.players:
                self.play_round(self.rounds[player.index + self.round_number * i], player)
                self.round_number += 1

    def play_round(self, round, player):
        print(f"\n{player.name}'s turn:")
        self.play_turn(player, round)
    
    def passive_turn(self, round, active_player):
        passive_players = [player for player in self.players if not player == active_player]
        for player in passive_players:
            player.action(round, round.throw_away_dice)

    def play_turn(self, player, round):
        print("Rolling dice...")
        round.roll_dice()
        player_actions = 3

        while player_actions > 0:
            print(f"\nActions remaining: {player_actions}")
            player.action(round, round.all_dice)
            player_actions -= 1

        print("End of the Game")

    def end_game(self):
        for player in self.players:
            scoreboard = ScoreBoard(player.boards)
            print(f"The final score of {player.name} is {scoreboard.get_total_score()}")
        
        print("")
        print("End of the Game")
            
        
 
class Player:
    def __init__(self, name, score, boards, index):
        self.name = name
        self.score = score
        self.boards = boards
        self.index = index

        self.bonusses = []

    def action(self, round, dice):
        usable_dice = dice
        bonus = []

        print("Usable dice are")
        for d in usable_dice:
            print(d.print_color_value())

        while usable_dice:
            chosen_dice = random.choice(usable_dice)

            if chosen_dice.color == "White":
                board = random.choice(self.boards)
            else:
                board = chosen_dice.get_board(self.boards)

            if board.color == "Blue":
                if board.available_spaces(board, round.white_dice.value + round.blue_dice.value):
                    print(board.available_spaces(board, round.white_dice.value + round.blue_dice.value))
                    print(f"Chosen dice value: {chosen_dice.value}")
                    print(f"Available spaces: {board.available_spaces(board, round.white_dice.value + round.blue_dice.value)}")
                    chosen_space = random.choice(board.available_spaces(board, chosen_dice.value))

                    round.choose_dice(chosen_dice)
                    board.cross_space(chosen_space, chosen_dice.value)
                    bonus = board.check_bonus(chosen_space)
                    break
            elif board.available_spaces(board, chosen_dice.value):
                chosen_space = random.choice(board.available_spaces(board, chosen_dice.value))
                round.choose_dice(chosen_dice)
                board.cross_space(chosen_space, chosen_dice.value)
                bonus = board.check_bonus(chosen_space)
                break
            else:
                usable_dice.remove(chosen_dice)

        if not usable_dice:
            if dice: 
                round.choose_dice(random.choice(dice))

        
        for b in bonus:
            self.bonusses.append(b)



                

            