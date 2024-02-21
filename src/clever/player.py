import random
import warnings

from clever.dice import Dice
from clever.space import Space
from clever.board import Board
from clever.round import Round
# from clever.src.ai import AI_Model

# class that defines a player that participates in the game
class Player:
    def __init__(self, name: str, score: int, boards: list[Board], index: int, AI_Model = None) -> None:
        self.name = name
        self.score = score
        self.boards = boards
        self.index = index
        self.reroll_count = 0
        self.plusOne_count = 0
        self.fox_count = 0
        self.AI_Model = AI_Model

        self.bonusses = []

    def get_reroll_count(self) -> int:
        return self.reroll_count 
    
    def get_plusOne_count(self) -> int:
        return self.plusOne_count 
    
    def get_fox_count(self) -> int:
        return self.fox_count 
    
    def set_reroll_count(self, newValue: int) -> None:
        self.reroll_count = newValue 
    
    def set_plusOne_count(self, newValue: int) -> None:
        self.plusOne_count = newValue
    
    def set_fox_count(self, newValue: int) -> None:
        self.fox_count = newValue

    def get_total_score(self) -> int: 
        total_score = 0
        lowest_score_board = 70
        for board in self.boards:
            total_score += board.get_score()
            if board.get_score() < lowest_score_board:
                lowest_score_board = board.get_score()

        total_score += lowest_score_board * self.fox_count
        
        return total_score
    
    def get_name(self):
        return self.name
    
    def player_choose_dice(self, dice: list[Dice]) -> Dice:
        return random.choice(dice)
    
    def player_choose_board(self, boards: list[Board]) -> Board:
        return random.choice(boards)
        
    def player_choose_space(self, available_spaces: list[Space]) -> Space:
        return random.choice(available_spaces)
    
    def player_choose_reroll(self) -> bool:
        if self.reroll_count < 1:
            warnings.warn("No reroll left, reroll_count of this player is non-positive", category=Warning)
        return random.choice()
    
    def player_choose_plusOne(self, dice: list[Dice]) -> Dice:
        if self.plusOne_count < 1:
            warnings.warn("No plusOne left, plusOne_count of this player is non-positive", category=Warning)
        return random.choice(dice)


    def choose_board(self, boards: list[Board], chosen_dice: Dice) -> Board:
        if chosen_dice.get_color() == "White":
            return self.player_choose_board(boards)
        else:
            return chosen_dice.get_board(boards)
    
    def choose_space(self, board: Board, chosen_dice: Dice, round: Round) -> Space:
        chosen_space = None
        available_spaces = None
        if board.color == "Blue":
            available_spaces = board.available_spaces(round.white_dice.value + round.blue_dice.value)  
        else:
            available_spaces = board.available_spaces(chosen_dice.value)
        
        if available_spaces:
            chosen_space = self.player_choose_space(available_spaces)
            chosen_space.cross(chosen_dice.get_value())

        return chosen_space
    
    

    def action(self, round: Round, dice: list[Dice]) -> Dice:
        usable_dice = dice
        bonus = []

        print("Usable dice are")
        for d in usable_dice:
            print(d.print_color_value())

        if usable_dice:
            chosen_dice = self.player_choose_dice(usable_dice)
            print(f"\n{self.name} choose {chosen_dice.print_color_value()}")

            chosen_board = self.choose_board(self.boards, chosen_dice)

            chosen_space = self.choose_space(chosen_board, chosen_dice, round)
            print(f"\nThe available spaces on the {chosen_board.print_color_value()} board is: {chosen_space}")
            if chosen_space:
                bonus = chosen_board.check_bonus(chosen_space)
                chosen_board.cross_space(chosen_space, chosen_dice.value)

                #bonusses is useless, need to change this soon
                if bonus:
                    for b in bonus:
                        self.bonusses.append(b)
                        print(f"\nActing on the {b} bonus")
                        chosen_space = b.power(player=self)


            return chosen_dice
        
        return None

    def inactive_turn(self, round: Round) -> None:
        print(f"\n Inactive turn of {self.name} \n")
        self.action(round, round.throw_away_dice)
